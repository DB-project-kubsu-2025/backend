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


@admin.action(description='Установить ml_service_category = HOBBIES')
def set_ml_category_hobbies(modeladmin, request, queryset):
    """Установить ml_service_category = HOBBIES"""
    queryset.update(ml_service_category=ProductCategory.HOBBIES)


@admin.action(description='Установить ml_service_category = FOODS')
def set_ml_category_foods(modeladmin, request, queryset):
    """Установить ml_service_category = FOODS"""
    queryset.update(ml_service_category=ProductCategory.FOODS)


@admin.action(description='Установить ml_service_category = HOUSEHOLD')
def set_ml_category_household(modeladmin, request, queryset):
    """Установить ml_service_category = HOUSEHOLD"""
    queryset.update(ml_service_category=ProductCategory.HOUSEHOLD)


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    """Админ для ProductCategory"""

    list_display = ['id', 'name', 'ml_service_category']
    search_fields = ('name', 'ml_service_category')
    list_filter = ['ml_service_category']
    actions = (
        set_ml_category_hobbies,
        set_ml_category_foods,
        set_ml_category_household,
    )


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
        'ml_service_id',
    ]
    list_display_links = ['id', 'director']
    raw_id_fields = ['director', 'main_office_filial']
    list_filter = ['main_office_filial', 'opened']


@admin.register(SpaceType)
class SpaceTypeAdmin(admin.ModelAdmin):
    """Админ для SpaceType"""

    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Space)
class SpaceAdmin(admin.ModelAdmin):
    """Админ для Space"""

    list_display = (
        'id',
        'storage',
        'space_type',
        'parent_space',
        'temp_min_c',
        'temp_max_c',
        'max_load',
        'dt_created',
    )
    list_filter = (
        'storage',
        'space_type',
    )
    search_fields = (
        'storage__name',
        'space_type__name',
    )
    raw_id_fields = (
        'storage',
        'space_type',
        'parent_space',
    )
    fieldsets = (
        (
            None,
            {
                'fields': (
                    'storage',
                    'space_type',
                    'parent_space',
                )
            },
        ),
        (
            'Условия хранения',
            {
                'fields': (
                    'temp_min_c',
                    'temp_max_c',
                    'max_load',
                )
            },
        ),
        (
            'Служебная информация',
            {
                'fields': (
                    'dt_created',
                    'dt_updated',
                )
            },
        ),
    )
    readonly_fields = (
        'dt_created',
        'dt_updated',
    )


@admin.register(InventoryLot)
class InventoryLotAdmin(admin.ModelAdmin):
    """Админ для InventoryLot"""

    list_display = (
        'id',
        'product',
        'manufacture_date',
        'expiry_date',
        'dt_created',
    )
    list_filter = (
        'product',
        'manufacture_date',
        'expiry_date',
    )
    search_fields = (
        'product__name',
    )
    raw_id_fields = (
        'product',
        'supply_product_lot',
    )
    fieldsets = (
        (
            None,
            {
                'fields': (
                    'product',
                    'supply_product_lot',
                )
            },
        ),
        (
            'Даты',
            {
                'fields': (
                    'manufacture_date',
                    'expiry_date',
                )
            },
        ),
        (
            'Служебная информация',
            {
                'fields': (
                    'dt_created',
                    'dt_updated',
                )
            },
        ),
    )
    readonly_fields = (
        'dt_created',
        'dt_updated',
    )


@admin.register(InventoryBalance)
class InventoryBalanceAdmin(admin.ModelAdmin):
    """Админ для InventoryBalance"""

    list_display = (
        'id',
        'inventory_lot',
        'storage',
        'space',
        'quantity',
        'dt_created',
        'dt_updated',
    )
    list_filter = (
        'storage',
        'space',
        'inventory_lot__product',
    )
    search_fields = (
        'inventory_lot__product__name',
        'space__space_type__name',
        'storage__name',
    )
    raw_id_fields = (
        'inventory_lot',
        'storage',
        'space',
    )
    readonly_fields = (
        'dt_created',
        'dt_updated',
    )



@admin.register(MovementType)
class MovementTypeAdmin(admin.ModelAdmin):
    """Админ для MovementType"""

    list_display = ('name', 'dt_created', 'dt_updated')
    search_fields = ('name',)
    ordering = ('name',)
    readonly_fields = ('dt_created', 'dt_updated')



@admin.register(InventoryMovement)
class InventoryMovementAdmin(admin.ModelAdmin):
    """Админ для InventoryMovement"""

    list_display = (
        'id',
        'inventory_lot',
        'storage',
        'space_from',
        'space_to',
        'movement_type',
        'created_by',
        'quantity',
        'dt_created',
        'dt_updated',
    )
    list_filter = (
        'storage',
        'movement_type',
        'created_by',
        'inventory_lot__product',
    )
    search_fields = (
        'inventory_lot__product__name',
        'storage__name',
        'space_from__space_type__name',
        'space_to__space_type__name',
        'created_by__username',
    )
    raw_id_fields = (
        'inventory_lot',
        'storage',
        'space_from',
        'space_to',
        'created_by',
        'movement_type',
        'supply',
        'sales_receipt',
        'writeoff_act',
    )
    readonly_fields = (
        'dt_created',
        'dt_updated',
    )


@admin.register(PriceList)
class PriceListAdmin(admin.ModelAdmin):
    """Админ для PriceList"""

    list_display = (
        'id',
        'storage',
        'received_at',
        'business_date',
        'status',
        'dt_created',
        'dt_updated',
    )
    list_filter = (
        'storage',
        'status',
        'business_date',
    )
    search_fields = (
        'storage__name',
    )
    raw_id_fields = (
        'storage',
    )
    readonly_fields = (
        'dt_created',
        'dt_updated',
    )


@admin.register(PriceListType)
class PriceListTypeAdmin(admin.ModelAdmin):
    """Админ для PriceListType"""

    list_display = (
        'name',
        'dt_created',
        'dt_updated',
    )

    search_fields = ('name',)
    ordering = ('name',)
    readonly_fields = (
        'dt_created',
        'dt_updated',
    )


@admin.register(PriceListBase)
class PriceListBaseAdmin(admin.ModelAdmin):
    """Админ для PriceListBase"""

    list_display = (
        'name',
        'is_active',
        'dt_created',
        'dt_updated',
    )
    list_filter = ('is_active',)
    search_fields = ('name',)
    ordering = ('name',)
    readonly_fields = (
        'dt_created',
        'dt_updated',
    )


@admin.register(PriceListProduct)
class PriceListProductAdmin(admin.ModelAdmin):
    """Админ для PriceListProduct"""

    list_display = (
        'id',
        'price_list',
        'product',
        'price_list_type',
        'price_list_base',
        'input_cost_vh',
        'regular_price',
        'final_price',
        'dt_created',
        'dt_updated',
    )
    list_filter = (
        'price_list__storage',
        'price_list_type',
        'price_list_base',
    )
    search_fields = (
        'product__name',
        'price_list__id',
    )
    raw_id_fields = (
        'price_list',
        'price_list_type',
        'price_list_base',
        'product',
    )
    readonly_fields = (
        'dt_created',
        'dt_updated',
    )


@admin.register(PricingConstraint)
class PricingConstraintAdmin(admin.ModelAdmin):
    """Админ для PricingConstraint"""

    list_display = (
        'id',
        'scope',
        'storage',
        'product_category',
        'product',
        'priority',
        'is_active',
        'max_daily_change_pct',
        'max_markup_pct',
        'dt_created',
        'dt_updated',
    )
    list_filter = (
        'scope',
        'is_active',
        'storage',
    )
    search_fields = (
        'storage__name',
        'product_category__name',
        'product__name',
    )
    raw_id_fields = (
        'storage',
        'product_category',
        'product',
    )
    readonly_fields = (
        'dt_created',
        'dt_updated',
    )



@admin.register(PricingRun)
class PricingRunAdmin(admin.ModelAdmin):
    """Админ для PricingRun"""

    list_display = (
        'id',
        'storage',
        'created_by',
        'status',
        'business_date',
        'started_at',
        'finished_at',
        'confirmed_at',
        'error_message',
        'dt_created',
        'dt_updated',
    )
    list_filter = (
        'storage',
        'status',
        'business_date',
        'created_by',
    )
    search_fields = (
        'storage__name',
        'created_by__username',
        'id',
    )
    raw_id_fields = (
        'storage',
        'created_by',
    )
    readonly_fields = (
        'dt_created',
        'dt_updated',
    )


@admin.register(StorePrice)
class StorePriceAdmin(admin.ModelAdmin):
    """Админ для StorePrice"""

    list_display = (
        'id',
        'pricing_run',
        'product',
        'business_date',
        'price_list_type',
        'price_list_base',
        'final_price',
        'is_sale_allowed',
        'block_reason',
        'dt_created',
        'dt_updated',
    )
    list_filter = (
        'pricing_run__storage',
        'price_list_type',
        'price_list_base',
        'is_sale_allowed',
        'business_date',
    )
    search_fields = (
        'product__name',
        'pricing_run__id',
    )
    raw_id_fields = (
        'pricing_run',
        'product',
        'price_list_type',
        'price_list_base',
    )
    readonly_fields = (
        'dt_created',
        'dt_updated',
    )


@admin.register(CouponDiscountType)
class CouponDiscountTypeAdmin(admin.ModelAdmin):
    """Админ для CouponDiscountType"""

    list_display = (
        'name',
        'dt_created',
        'dt_updated',
    )
    search_fields = ('name',)
    ordering = ('name',)
    readonly_fields = (
        'dt_created',
        'dt_updated',
    )


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    """Админ для Coupon"""

    list_display = (
        'id',
        'storage',
        'product',
        'discount_type',
        'value',
        'valid_from',
        'valid_to',
        'min_quantity',
        'is_active',
        'dt_created',
        'dt_updated',
    )
    list_filter = (
        'storage',
        'discount_type',
        'is_active',
        'valid_from',
        'valid_to',
    )
    search_fields = (
        'storage__name',
        'product__name',
        'discount_type__name',
    )
    raw_id_fields = (
        'storage',
        'product',
        'discount_type',
    )
    readonly_fields = (
        'dt_created',
        'dt_updated',
    )


@admin.register(PaymentMethod)
class PaymentMethodAdmin(admin.ModelAdmin):
    """Админ для PaymentMethod"""

    list_display = (
        'name',
        'dt_created',
        'dt_updated',
    )
    search_fields = ('name',)
    ordering = ('name',)
    readonly_fields = (
        'dt_created',
        'dt_updated',
    )


@admin.register(SaleReceipt)
class SaleReceiptAdmin(admin.ModelAdmin):
    """Админ для SaleReceipt"""

    list_display = (
        'id',
        'storage',
        'cashier',
        'time_session',
        'payment_method',
        'status',
        'opened_at',
        'closed_at',
        'total_gross',
        'total_discount',
        'total_payable',
        'paid_amount',
        'paid_at',
        'dt_created',
        'dt_updated',
    )
    list_filter = (
        'storage',
        'cashier',
        'time_session',
        'payment_method',
        'status',
        'opened_at',
        'closed_at',
    )
    search_fields = (
        'storage__name',
        'cashier__username',
        'time_session__id',
        'payment_method__name',
    )
    raw_id_fields = (
        'storage',
        'cashier',
        'time_session',
        'payment_method',
    )
    readonly_fields = (
        'dt_created',
        'dt_updated',
    )


@admin.register(SalesReceiptLine)
class SalesReceiptLineAdmin(admin.ModelAdmin):
    """Админ для SalesReceiptLine"""

    list_display = (
        'id',
        'sale_receipt',
        'inventory_lot',
        'coupon',
        'price_list_type',
        'price_list_base',
        'quantity',
        'unit_price',
        'line_discount',
        'line_total',
        'dt_created',
        'dt_updated',
    )
    list_filter = (
        'price_list_type',
        'price_list_base',
        'sale_receipt__storage',
    )
    search_fields = (
        'sale_receipt__id',
        'inventory_lot__product__name',
        'coupon__id',
    )
    raw_id_fields = (
        'sale_receipt',
        'inventory_lot',
        'coupon',
        'price_list_type',
        'price_list_base',
    )
    readonly_fields = (
        'dt_created',
        'dt_updated',
    )



@admin.register(StopList)
class StopListAdmin(admin.ModelAdmin):
    """Админ для StopList"""

    list_display = (
        'id',
        'storage',
        'pricing_run',
        'created_by',
        'business_date',
        'status',
        'sent_to_hq_at',
        'hq_comment',
        'closed_at',
        'dt_created',
        'dt_updated',
    )
    list_filter = (
        'storage',
        'status',
        'created_by',
        'business_date',
    )
    search_fields = (
        'storage__name',
        'created_by__username',
        'pricing_run__id',
    )
    raw_id_fields = (
        'storage',
        'pricing_run',
        'created_by',
    )
    readonly_fields = (
        'dt_created',
        'dt_updated',
    )


@admin.register(StopListReason)
class StopListReasonAdmin(admin.ModelAdmin):
    """Админ для StopListReason"""

    list_display = (
        'name',
        'dt_created',
        'dt_updated',
    )
    search_fields = ('name',)
    ordering = ('name',)
    readonly_fields = (
        'dt_created',
        'dt_updated',
    )


@admin.register(StopListProduct)
class StopListProductAdmin(admin.ModelAdmin):
    """Админ для StopListProduct"""

    list_display = (
        'id',
        'stop_list',
        'product',
        'price_list_type',
        'price_list_base',
        'stop_list_reason',
        'status',
        'input_cost_vh',
        'yesterday_price',
        'candidate_price',
        'final_price_applied',
        'dt_created',
        'dt_updated',
    )
    list_filter = (
        'status',
        'stop_list__storage',
        'price_list_type',
        'stop_list_reason',
    )
    search_fields = (
        'product__name',
        'stop_list__id',
        'stop_list__storage__name',
    )
    raw_id_fields = (
        'stop_list',
        'product',
        'price_list_type',
        'price_list_base',
        'stop_list_reason',
    )
    readonly_fields = (
        'dt_created',
        'dt_updated',
    )


@admin.register(StockTakeType)
class StockTakeTypeAdmin(admin.ModelAdmin):
    """Админ для StockTakeType"""

    list_display = (
        'name',
        'is_active',
        'dt_created',
        'dt_updated',
    )
    list_filter = ('is_active',)
    search_fields = ('name',)
    ordering = ('name',)
    readonly_fields = (
        'dt_created',
        'dt_updated',
    )


@admin.register(StockTake)
class StockTakeAdmin(admin.ModelAdmin):
    """Админ для StockTake"""

    list_display = (
        'id',
        'storage',
        'space',
        'stocktake_type',
        'created_by',
        'reviewed_by',
        'status',
        'business_date',
        'snapshot_at',
        'approved_at',
        'director_comment',
        'reviewed_at',
        'reviewer_comment',
        'closed_at',
        'dt_created',
        'dt_updated',
    )
    list_filter = (
        'storage',
        'stocktake_type',
        'status',
        'created_by',
        'reviewed_by',
        'business_date',
    )
    search_fields = (
        'storage__name',
        'space__space_type__name',
        'created_by__username',
        'reviewed_by__username',
    )
    raw_id_fields = (
        'storage',
        'space',
        'stocktake_type',
        'created_by',
        'reviewed_by',
    )
    readonly_fields = (
        'dt_created',
        'dt_updated',
    )


@admin.register(StockTakeLine)
class StockTakeLineAdmin(admin.ModelAdmin):
    """Админ для StockTakeLine"""

    list_display = (
        'id',
        'stocktake',
        'space',
        'inventory_lot',
        'counted_by',
        'counted_at',
        'quantity_expected',
        'quantity_actual',
        'is_expired',
        'comment',
        'dt_created',
        'dt_updated',
    )
    list_filter = (
        'stocktake__storage',
        'space',
        'counted_by',
        'is_expired',
    )
    search_fields = (
        'stocktake__id',
        'inventory_lot__product__name',
        'space__space_type__name',
        'counted_by__username',
    )
    raw_id_fields = (
        'stocktake',
        'space',
        'inventory_lot',
        'counted_by',
    )
    readonly_fields = (
        'dt_created',
        'dt_updated',
    )


@admin.register(StockTakeAdjustment)
class StockTakeAdjustmentAdmin(admin.ModelAdmin):
    """Админ для StockTakeAdjustment"""

    list_display = (
        'id',
        'stocktake',
        'stocktake_line',
        'inventory_movement',
        'dt_created',
        'dt_updated',
    )
    list_filter = (
        'stocktake__storage',
    )
    search_fields = (
        'stocktake__id',
        'stocktake_line__id',
        'inventory_movement__id',
    )
    raw_id_fields = (
        'stocktake',
        'stocktake_line',
        'inventory_movement',
    )
    readonly_fields = (
        'dt_created',
        'dt_updated',
    )


@admin.register(WriteoffReason)
class WriteoffReasonAdmin(admin.ModelAdmin):
    """Админ для WriteoffReason"""

    list_display = (
        'name',
        'is_active',
        'requires_photo',
        'dt_created',
        'dt_updated',
    )
    list_filter = (
        'is_active',
        'requires_photo',
    )
    search_fields = ('name',)
    ordering = ('name',)
    readonly_fields = (
        'dt_created',
        'dt_updated',
    )


@admin.register(WriteOffAct)
class WriteOffActAdmin(admin.ModelAdmin):
    """Админ для WriteOffAct"""

    list_display = (
        'id',
        'storage',
        'writeoff_reason',
        'created_by',
        'reviewed_by',
        'status',
        'submitted_at',
        'submit_comment',
        'reviewed_at',
        'review_comment',
        'approved_at',
        'posted_at',
        'dt_created',
        'dt_updated',
    )
    list_filter = (
        'storage',
        'status',
        'writeoff_reason',
        'created_by',
        'reviewed_by',
    )
    search_fields = (
        'storage__name',
        'writeoff_reason__name',
        'created_by__username',
        'reviewed_by__username',
    )
    raw_id_fields = (
        'storage',
        'writeoff_reason',
        'created_by',
        'reviewed_by',
    )
    readonly_fields = (
        'dt_created',
        'dt_updated',
    )


@admin.register(WriteoffLine)
class WriteoffLineAdmin(admin.ModelAdmin):
    """Админ для WriteoffLine"""

    list_display = (
        'id',
        'writeoff_act',
        'space',
        'inventory_lot',
        'quantity',
        'comment',
        'dt_created',
        'dt_updated',
    )
    list_filter = (
        'writeoff_act__storage',
        'space',
    )
    search_fields = (
        'writeoff_act__id',
        'inventory_lot__product__name',
        'space__space_type__name',
    )
    raw_id_fields = (
        'writeoff_act',
        'space',
        'inventory_lot',
    )
    readonly_fields = (
        'dt_created',
        'dt_updated',
    )


@admin.register(WriteoffAttachment)
class WriteoffAttachmentAdmin(admin.ModelAdmin):
    """Админ для WriteoffAttachment"""

    list_display = (
        'id',
        'writeoff_act',
        'image',
        'dt_created',
        'dt_updated',
    )
    list_filter = ('writeoff_act__storage',)
    search_fields = ('writeoff_act__id',)
    raw_id_fields = ('writeoff_act',)
    readonly_fields = (
        'dt_created',
        'dt_updated',
    )


@admin.register(WriteoffPosting)
class WriteoffPostingAdmin(admin.ModelAdmin):
    """Админ для WriteoffPosting"""

    list_display = (
        'id',
        'writeoff_act',
        'writeoff_line',
        'inventory_movement',
        'dt_created',
        'dt_updated',
    )
    list_filter = (
        'writeoff_act__storage',
    )
    search_fields = (
        'writeoff_act__id',
        'writeoff_line__id',
        'inventory_movement__id',
    )
    raw_id_fields = (
        'writeoff_act',
        'writeoff_line',
        'inventory_movement',
    )
    readonly_fields = (
        'dt_created',
        'dt_updated',
    )
