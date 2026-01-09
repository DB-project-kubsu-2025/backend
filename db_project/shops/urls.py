from django.urls import path, include
from rest_framework.routers import SimpleRouter

from shops.views import (
    ProductUnitViewSet,
    ProductCategoryViewSet,
    StorageTypeViewSet,
    SpaceTypeViewSet,
    MovementTypeViewSet,
    PriceListTypeViewSet,
    PriceListBaseViewSet,
    CouponDiscountTypeViewSet,
    PaymentMethodViewSet,
    StopListReasonViewSet,
    StockTakeTypeViewSet,
    WriteoffReasonViewSet,
    StorageProfileViewSet,
    SpaceViewSet,
    InventoryLotViewSet,
    StorageViewSet,
    ProductMediaViewSet,
    ProductViewSet,
)

shops_router = SimpleRouter()
shops_router.register('products/units', ProductUnitViewSet)
shops_router.register('products/categories', ProductCategoryViewSet)
shops_router.register('products/media', ProductMediaViewSet)
shops_router.register('products', ProductViewSet)
shops_router.register('storages/profiles', StorageProfileViewSet)
shops_router.register('storages/types', StorageTypeViewSet)
shops_router.register('storages/spaces/types', SpaceTypeViewSet)
shops_router.register('storages/spaces', SpaceViewSet)
shops_router.register('storages/inventory_lots', InventoryLotViewSet)
shops_router.register('storages', StorageViewSet)
shops_router.register('movements/types', MovementTypeViewSet)
shops_router.register('price-lists/types', PriceListTypeViewSet)
shops_router.register('price-lists/bases', PriceListBaseViewSet)
shops_router.register('coupons/discounts/types', CouponDiscountTypeViewSet)
shops_router.register('payments/methods', PaymentMethodViewSet)
shops_router.register('stop-lists/reasons', StopListReasonViewSet)
shops_router.register('stock-takes/types', StockTakeTypeViewSet)
shops_router.register('writeoffs/reasons', WriteoffReasonViewSet)

urlpatterns = [
    path('', include(shops_router.urls)),
]
