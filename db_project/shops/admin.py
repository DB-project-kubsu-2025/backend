from django.contrib import admin

from shops.models import (
    ProductUnit,
    ProductCategory,
    Product,
    StorageProfile,
    ProductMedia,
    StorageType,
    Storage,
    SpaceType,
    Space,
    InventoryLot,
    InventoryBalance,
    MovementType,
    InventoryMovement,
    PriceList,
    PriceListType,
    PriceListBase,
    PriceListProduct,
    PricingConstraint,
    PricingRun,
    StorePrice,
    CouponDiscountType,
    Coupon,
    PaymentMethod,
    SaleReceipt,
    SalesReceiptLine,
    StopList,
    StopListReason,
    StopListProduct,
    StockTakeType,
    StockTakeLine,
    StockTakeAdjustment,
    WriteoffReason,
    WriteOffAct,
    WriteoffLine,
    WriteoffAttachment,
    WriteoffPosting,
    StockTake,
)

@admin.register(ProductUnit)
class ProductUnitAdmin(admin.ModelAdmin):
    """Админ для ProductUnit"""

    list_display = ['id', 'name']


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    """Админ для ProductCategory"""

    list_display = ['id', 'name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Админ для Product"""

    list_display = ['id', 'name', 'unit', 'category', 'expiration_days', 'producer_name', 'country_name']
    raw_id_fields = ['category', 'unit']
    list_filter = ['category', 'unit']


@admin.register(StorageProfile)
class StorageProfileAdmin(admin.ModelAdmin):
    """Админ для StorageProfile"""

    list_display = ['id', 'product', 'weight', 'temp_min_c', 'temp_max_c', 'light_sensitive']
    raw_id_fields = ['product']


@admin.register(ProductMedia)
class ProductMediaAdmin(admin.ModelAdmin):
    """Админ для ProductMedia"""

    list_display = ['id', 'product']
    raw_id_fields = ['product']
    list_filter = ['product']


@admin.register(StorageType)
class StorageTypeAdmin(admin.ModelAdmin):
    """Админ для StorageType"""

    list_display = ['id', 'name']


@admin.register(Storage)
class StorageAdmin(admin.ModelAdmin):
    """Админ для Storage"""

    list_display = [
        'id',
        'director',
        'main_office_filial',
        'storage_type',
        'cadastral_number',
        'opened',
        'approved_by_main_company',
        'area',
    ]
    raw_id_fields = ['director', 'main_office_filial']
    list_filter = ['main_office_filial', 'opened']


@admin.register(SpaceType)
class SpaceTypeAdmin(admin.ModelAdmin):
    """Админ для SpaceType"""


@admin.register(Space)
class SpaceAdmin(admin.ModelAdmin):
    """Админ для Space"""


@admin.register(InventoryLot)
class InventoryLotAdmin(admin.ModelAdmin):
    """Админ для InventoryLot"""


@admin.register(InventoryBalance)
class InventoryBalanceAdmin(admin.ModelAdmin):
    """Админ для InventoryBalance"""


@admin.register(MovementType)
class MovementTypeAdmin(admin.ModelAdmin):
    """Админ для MovementType"""


@admin.register(InventoryMovement)
class InventoryMovementAdmin(admin.ModelAdmin):
    """Админ для InventoryMovement"""


@admin.register(PriceList)
class PriceListAdmin(admin.ModelAdmin):
    """Админ для PriceList"""


@admin.register(PriceListType)
class PriceListTypeAdmin(admin.ModelAdmin):
    """Админ для PriceListType"""


@admin.register(PriceListBase)
class PriceListBaseAdmin(admin.ModelAdmin):
    """Админ для PriceListBase"""


@admin.register(PriceListProduct)
class PriceListProductAdmin(admin.ModelAdmin):
    """Админ для PriceListProduct"""


@admin.register(PricingConstraint)
class PricingConstraintAdmin(admin.ModelAdmin):
    """Админ для PricingConstraint"""


@admin.register(PricingRun)
class PricingRunAdmin(admin.ModelAdmin):
    """Админ для PricingRun"""


@admin.register(StorePrice)
class StorePriceAdmin(admin.ModelAdmin):
    """Админ для StorePrice"""


@admin.register(CouponDiscountType)
class CouponDiscountTypeAdmin(admin.ModelAdmin):
    """Админ для CouponDiscountType"""


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    """Админ для Coupon"""


@admin.register(PaymentMethod)
class PaymentMethodAdmin(admin.ModelAdmin):
    """Админ для PaymentMethod"""


@admin.register(SaleReceipt)
class SaleReceiptAdmin(admin.ModelAdmin):
    """Админ для SaleReceipt"""


@admin.register(SalesReceiptLine)
class SalesReceiptLineAdmin(admin.ModelAdmin):
    """Админ для SalesReceiptLine"""


@admin.register(StopList)
class StopListAdmin(admin.ModelAdmin):
    """Админ для StopList"""


@admin.register(StopListReason)
class StopListReasonAdmin(admin.ModelAdmin):
    """Админ для StopListReason"""


@admin.register(StopListProduct)
class StopListProductAdmin(admin.ModelAdmin):
    """Админ для StopListProduct"""


@admin.register(StockTakeType)
class StockTakeTypeAdmin(admin.ModelAdmin):
    """Админ для StockTakeType"""


@admin.register(StockTake)
class StockTakeAdmin(admin.ModelAdmin):
    """Админ для StockTake"""


@admin.register(StockTakeLine)
class StockTakeLineAdmin(admin.ModelAdmin):
    """Админ для StockTakeLine"""


@admin.register(StockTakeAdjustment)
class StockTakeAdjustmentAdmin(admin.ModelAdmin):
    """Админ для StockTakeAdjustment"""


@admin.register(WriteoffReason)
class WriteoffReasonAdmin(admin.ModelAdmin):
    """Админ для WriteoffReason"""


@admin.register(WriteOffAct)
class WriteOffActAdmin(admin.ModelAdmin):
    """Админ для WriteOffAct"""


@admin.register(WriteoffLine)
class WriteoffLineAdmin(admin.ModelAdmin):
    """Админ для WriteoffLine"""


@admin.register(WriteoffAttachment)
class WriteoffAttachmentAdmin(admin.ModelAdmin):
    """Админ для WriteoffAttachment"""


@admin.register(WriteoffPosting)
class WriteoffPostingAdmin(admin.ModelAdmin):
    """Админ для WriteoffPosting"""
