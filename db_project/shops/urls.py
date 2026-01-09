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
    ProductInventoryLotViewSet,
    InventoryBalanceViewSet,
    InventoryMovementViewSet,
    PriceListViewSet,
    PriceListProductViewSet,
    PricingConstraintViewSet,
    PricingRunViewSet,
    StorePriceViewSet,
    CouponViewSet,
    SaleReceiptViewSet,
    SalesReceiptLineViewSet,
    StopListViewSet,
    StopListProductViewSet,
    StockTakeViewSet,
    StockTakeLineViewSet,
    StockTakeAdjustmentViewSet,
    WriteOffActViewSet,
    WriteoffLineViewSet,
    WriteoffAttachmentViewSet,
    WriteoffPostingViewSet,
)

shops_router = SimpleRouter()
shops_router.register('products/units', ProductUnitViewSet)
shops_router.register('products/categories', ProductCategoryViewSet)
shops_router.register('products/media', ProductMediaViewSet)
shops_router.register('products', ProductViewSet)
shops_router.register('products/inventory_lots', ProductInventoryLotViewSet)
shops_router.register('storages/profiles', StorageProfileViewSet)
shops_router.register('storages/types', StorageTypeViewSet)
shops_router.register('storages/spaces/types', SpaceTypeViewSet)
shops_router.register('storages/spaces', SpaceViewSet)
shops_router.register('storages/inventory_balances', InventoryBalanceViewSet)
shops_router.register('storages/inventory_movements', InventoryMovementViewSet)
shops_router.register('storages/inventory_lots', InventoryLotViewSet)
shops_router.register('storages', StorageViewSet)
shops_router.register('movements/types', MovementTypeViewSet)
shops_router.register('price-lists', PriceListViewSet)
shops_router.register('price-lists/products', PriceListProductViewSet)
shops_router.register('price-lists/types', PriceListTypeViewSet)
shops_router.register('price-lists/bases', PriceListBaseViewSet)
shops_router.register('pricing/constraints', PricingConstraintViewSet)
shops_router.register('pricing/runs', PricingRunViewSet)
shops_router.register('pricing/store_prices', StorePriceViewSet)
shops_router.register('coupons', CouponViewSet)
shops_router.register('coupons/discounts/types', CouponDiscountTypeViewSet)
shops_router.register('sales/receipts', SaleReceiptViewSet)
shops_router.register('sales/receipt_lines', SalesReceiptLineViewSet)
shops_router.register('payments/methods', PaymentMethodViewSet)
shops_router.register('stop-lists', StopListViewSet)
shops_router.register('stop-lists/products', StopListProductViewSet)
shops_router.register('stop-lists/reasons', StopListReasonViewSet)
shops_router.register('stock-takes', StockTakeViewSet)
shops_router.register('stock-takes/lines', StockTakeLineViewSet)
shops_router.register('stock-takes/adjustments', StockTakeAdjustmentViewSet)
shops_router.register('stock-takes/types', StockTakeTypeViewSet)
shops_router.register('writeoffs', WriteOffActViewSet)
shops_router.register('writeoffs/lines', WriteoffLineViewSet)
shops_router.register('writeoffs/attachments', WriteoffAttachmentViewSet)
shops_router.register('writeoffs/postings', WriteoffPostingViewSet)
shops_router.register('writeoffs/reasons', WriteoffReasonViewSet)

urlpatterns = [
    path('', include(shops_router.urls)),
]
