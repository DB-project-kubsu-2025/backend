# supplies/signals.py
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from supplies.models import SupplyProductLot, SupplyDiscrepancy
from supplies.services.workflow import recalc_supply_product


@receiver(post_save, sender=SupplyProductLot)
@receiver(post_delete, sender=SupplyProductLot)
def lot_changed(sender, instance: SupplyProductLot, **kwargs):
    recalc_supply_product(instance.supply_product_id)


@receiver(post_save, sender=SupplyDiscrepancy)
@receiver(post_delete, sender=SupplyDiscrepancy)
def discrepancy_changed(sender, instance: SupplyDiscrepancy, **kwargs):
    recalc_supply_product(instance.supply_product_lot.supply_product_id)