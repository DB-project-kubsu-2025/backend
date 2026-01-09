from django.urls import path, include
from rest_framework.routers import SimpleRouter

from supplies.views import (
    SupplierViewSet,
    SupplierContactViewSet,
    SupplyContractViewSet,
    SupplyContractProductViewSet,
)

router = SimpleRouter()
router.register("suppliers", SupplierViewSet)
router.register("suppliers/contacts", SupplierContactViewSet)
router.register("contracts", SupplyContractViewSet)
router.register("contracts/products", SupplyContractProductViewSet)

urlpatterns = [
    path("", include(router.urls)),
]