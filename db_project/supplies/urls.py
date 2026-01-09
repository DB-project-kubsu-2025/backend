from django.urls import path, include
from rest_framework.routers import SimpleRouter

from supplies.views.private import (
    SupplierViewSet,
    SupplierContactViewSet,
    SupplyContractViewSet,
    SupplyContractProductViewSet,
    
    SupplyViewSet,
    SupplyProductViewSet,
    SupplyProductLotViewSet,
    DiscrepancyReasonViewSet,
    SupplyDiscrepancyViewSet,
    DiscrepancyAttachmentViewSet,
)

router = SimpleRouter()
router.register("suppliers", SupplierViewSet)
router.register("suppliers/contacts", SupplierContactViewSet)
router.register("contracts", SupplyContractViewSet)
router.register("contracts/products", SupplyContractProductViewSet)
router.register("supplies", SupplyViewSet)
router.register("supply-products", SupplyProductViewSet)
router.register("supply-product-lots", SupplyProductLotViewSet)
router.register("discrepancy-reasons", DiscrepancyReasonViewSet)
router.register("discrepancies", SupplyDiscrepancyViewSet)
router.register("discrepancy-attachments", DiscrepancyAttachmentViewSet)

urlpatterns = [
    path("", include(router.urls)),
]