# supplies/services/posting.py

from __future__ import annotations

from dataclasses import dataclass

from django.db import transaction
from django.utils import timezone

from shops.models import (
    InventoryLot,
    InventoryBalance,
    InventoryMovement,
    MovementType,
    SpaceType,
    Space,
)

from supplies.models import Supply, SupplyProductLot


@dataclass
class PostingResult:
    created_inventory_lots: int = 0
    created_balances: int = 0
    created_movements: int = 0


def _get_or_create_receiving_space(storage) -> Space:
    """
    Создаём/берём "зону приёмки" в конкретном хранилище.
    """
    st, _ = SpaceType.objects.get_or_create(name="Приёмка")

    space = Space.objects.filter(storage=storage, space_type=st).first()
    if space:
        return space

    # В Space обязательные поля: temp_min_c, temp_max_c, max_load
    # Для учебного проекта ставим дефолты.
    return Space.objects.create(
        storage=storage,
        space_type=st,
        parent_space=None,
        temp_min_c=0,
        temp_max_c=25,
        max_load=9999,
    )


def _get_or_create_supply_movement_type() -> MovementType:
    mt, _ = MovementType.objects.get_or_create(name="Поставка")
    return mt


@transaction.atomic
def post_supply_to_inventory(supply: Supply, actor_employee) -> PostingResult:
    """
    Проведение поставки в складские сущности shops.
    Делает:
      - InventoryLot (по SupplyProductLot)
      - InventoryBalance (кладём в Space "Приёмка")
      - InventoryMovement (тип "Поставка")

    Идемпотентно: если уже есть InventoryLot по SupplyProductLot — повторно не создаём.
    """
    if supply.status != Supply.APPROVED:
        raise ValueError("Нельзя проводить поставку, пока она не APPROVED")

    receiving_space = _get_or_create_receiving_space(supply.storage)
    movement_type = _get_or_create_supply_movement_type()

    res = PostingResult()

    lots = (
        SupplyProductLot.objects
        .select_related("supply_product", "supply_product__supply", "supply_product__product")
        .filter(supply_product__supply_id=supply.id)
    )

    for spl in lots:
        inv_lot, created = InventoryLot.objects.get_or_create(
            supply_product_lot=spl,
            defaults={
                "product": spl.supply_product.product,
                "manufacture_date": spl.manufacture_date,
                "expiry_date": spl.expiry_date_actual,
            },
        )
        if created:
            res.created_inventory_lots += 1

        # Баланс в зоне приёмки: если уже есть — просто обновим количество
        bal, created_bal = InventoryBalance.objects.get_or_create(
            inventory_lot=inv_lot,
            storage=supply.storage,
            space=receiving_space,
            defaults={"quantity": spl.quantity_actual},
        )
        if created_bal:
            res.created_balances += 1
        else:
            # если вдруг проводили частично — приводим к факту
            if bal.quantity != spl.quantity_actual:
                bal.quantity = spl.quantity_actual
                bal.save(update_fields=["quantity"])

        # Движение "Поставка": не плодим дубли
        mv_exists = InventoryMovement.objects.filter(
            inventory_lot=inv_lot,
            storage=supply.storage,
            movement_type=movement_type,
            supply=supply,
            quantity=spl.quantity_actual,
            space_from__isnull=True,
            space_to=receiving_space,
        ).exists()

        if not mv_exists:
            InventoryMovement.objects.create(
                inventory_lot=inv_lot,
                storage=supply.storage,
                space_from=None,                 # "Пустое, если поставка"
                space_to=receiving_space,        # кладём в приёмку
                created_by=actor_employee,
                movement_type=movement_type,
                supply=supply,
                sales_receipt=None,
                writeoff_act=None,
                quantity=spl.quantity_actual,
            )
            res.created_movements += 1

    return res