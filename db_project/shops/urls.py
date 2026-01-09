from django.urls import path, include
from rest_framework.routers import SimpleRouter

from shops.views import (
    GetProductUnit,
    GetProductCategory,
    GetStorageType,
    GetSpaceType,
    GetMovementType,
    GetPriceListType,
    GetPriceListBase,
    GetCouponDiscountType,
    GetPaymentMethod,
    GetStopListReason,
    GetStockTakeType,
    GetWriteoffReason,
    GetStorageProfile,
    SpaceViewSet,
    InventoryLotViewSet,
    StorageViewSet,
    ProductMediaViewSet,
    ProductViewSet,
)

shops_router = SimpleRouter()
shops_router.register('products/units', GetProductUnit)
shops_router.register('products/categories', GetProductCategory)
shops_router.register('products/media', ProductMediaViewSet)
shops_router.register('products', ProductViewSet)
shops_router.register('storages/profiles', GetStorageProfile)
shops_router.register('storages/types', GetStorageType)
shops_router.register('storages/spaces/types', GetSpaceType)
shops_router.register('storages/spaces', SpaceViewSet)
shops_router.register('storages/inventory_lots', InventoryLotViewSet)
shops_router.register('storages', StorageViewSet)
shops_router.register('movements/types', GetMovementType)
shops_router.register('price-lists/types', GetPriceListType)
shops_router.register('price-lists/bases', GetPriceListBase)
shops_router.register('coupons/discounts/types', GetCouponDiscountType)
shops_router.register('payments/methods', GetPaymentMethod)
shops_router.register('stop-lists/reasons', GetStopListReason)
shops_router.register('stock-takes/types', GetStockTakeType)
shops_router.register('writeoffs/reasons', GetWriteoffReason)

urlpatterns = [
    path('', include(shops_router.urls)),
]
