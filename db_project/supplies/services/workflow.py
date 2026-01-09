# supplies/services/workflow.py
from __future__ import annotations

from django.db.models import Sum
from django.utils import timezone

from supplies.models import Supply, SupplyProduct, SupplyProductLot, SupplyDiscrepancy


def recalc_supply_product(supply_product_id: int) -> None:
    """
    Пересчитать:
    - quantity_actual_total (сумма лотов)
    - requires_review
    - status (ok / has_issues / resolved)
    """
    sp = SupplyProduct.objects.select_related("supply").get(id=supply_product_id)

    total = (
        SupplyProductLot.objects.filter(supply_product_id=sp.id)
        .aggregate(s=Sum("quantity_actual"))
        .get("s")
        or 0
    )

    # есть ли “проблемные” лоты (повреждения) или несоответствия
    has_damaged_lots = SupplyProductLot.objects.filter(
        supply_product_id=sp.id,
        packaging_condition=SupplyProductLot.DAMAGED,
    ).exists()

    has_unresolved_discrepancies = SupplyDiscrepancy.objects.filter(
        supply_product_lot__supply_product_id=sp.id,
    ).exclude(status=SupplyDiscrepancy.RESOLVED).exists()

    has_any_discrepancies = SupplyDiscrepancy.objects.filter(
        supply_product_lot__supply_product_id=sp.id,
    ).exists()

    quantities_match = (total == sp.quantity_expected)

    requires_review = has_damaged_lots or has_unresolved_discrepancies or (not quantities_match)

    if has_unresolved_discrepancies or (not quantities_match):
        new_status = SupplyProduct.HAS_ISSUES
    else:
        # если несоответствия были, но все resolved -> RESOLVED, иначе OK
        new_status = SupplyProduct.RESOLVED if has_any_discrepancies else SupplyProduct.OK

    SupplyProduct.objects.filter(id=sp.id).update(
        quantity_actual_total=total,
        requires_review=requires_review,
        status=new_status,
    )

    # после пересчёта продукта — можно пересчитать статусы поставки
    recalc_supply(sp.supply_id)


def recalc_supply(supply_id: int) -> None:
    """
    Авто-поддержка статуса поставки:
    - если есть нерешённые несоответствия -> PENDING_APPROVAL (если сейчас IN_RECEIVING)
    - если всё ок -> можно оставаться IN_RECEIVING/APPROVED, закрытие руками
    """
    supply = Supply.objects.get(id=supply_id)

    has_unresolved = SupplyDiscrepancy.objects.filter(
        supply_product_lot__supply_product__supply_id=supply_id
    ).exclude(status=SupplyDiscrepancy.RESOLVED).exists()

    # Не ломаем “ручные” статусы, но помогаем:
    if supply.status == Supply.IN_RECEIVING and has_unresolved:
        Supply.objects.filter(id=supply_id).update(status=Supply.PENDING_APPROVAL)


def set_discrepancy_decision(discrepancy: SupplyDiscrepancy, user, status: str, comment: str = "") -> None:
    SupplyDiscrepancy.objects.filter(id=discrepancy.id).update(
        status=status,
        decided_by=getattr(user, "employee", None),
        decided_at=timezone.now(),
        decision_comment=comment or "",
    )