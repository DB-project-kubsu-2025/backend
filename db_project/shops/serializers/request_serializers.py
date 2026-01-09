from drf_spectacular.utils import OpenApiExample, extend_schema_serializer
from rest_framework import serializers
from shops.models import (
    Space,
    InventoryLot,
    Storage,
    ProductMedia,
    Product,
    ProductUnit,
    ProductCategory,
    WriteoffReason,
    StockTakeType,
    StopListReason,
    PaymentMethod,
    CouponDiscountType,
    PriceListBase,
    PriceListType,
    MovementType,
    SpaceType,
    StorageType,
    StorageProfile,
    InventoryBalance,
    InventoryMovement,
    PriceList,
    PriceListProduct,
    PricingConstraint,
    PricingRun,
    StorePrice,
    Coupon,
    SaleReceipt,
    SalesReceiptLine,
    StopList,
    StopListProduct,
    StockTake,
    StockTakeLine,
    StockTakeAdjustment,
    WriteOffAct,
    WriteoffLine,
    WriteoffAttachment,
    WriteoffPosting,
    ProductInventoryLot,
)


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            'Пример запроса на создание медиа для товара',
            description='Базовый запрос',
            value={
                'product': 1,
                'image': 'binary multipart/form-data',
            },
            request_only=True,
        ),
    ],
)
class ProductMediaRequestSerializer(serializers.ModelSerializer):
    """Сериализатор запроса для создания/обновления ProductMedia"""

    class Meta:
        model = ProductMedia
        fields = [
            'product',
            'image',
        ]


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            'Пример запроса на создание хранилища',
            description='Базовый запрос',
            value={
                'director': 1,
                'main_office_filial': 2,
                'storage_type': 3,
                'cadastral_number': '77:01:0001001:1001',
                'approved_by_main_company': True,
                'opened': True,
                'area': 500,
                'utilization_percent': 75,
            },
            request_only=True,
        ),
    ],
)
class StorageRequestSerializer(serializers.ModelSerializer):
    """Сериализатор запроса для создания/обновления Storage"""

    class Meta:
        model = Storage
        fields = [
            'director',
            'main_office_filial',
            'storage_type',
            'cadastral_number',
            'approved_by_main_company',
            'opened',
            'area',
            'utilization_percent',
        ]


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            'Пример запроса на создание места хранения',
            description='Базовый запрос',
            value={
                'storage': 1,
                'space_type': 2,
                'parent_space': 3,
                'temp_min_c': 2,
                'temp_max_c': 6,
                'max_load': 100,
            },
            request_only=True,
        ),
    ],
)
class SpaceRequestSerializer(serializers.ModelSerializer):
    """Сериализатор запроса для создания/обновления Space"""

    class Meta:
        model = Space
        fields = [
            'storage',
            'space_type',
            'parent_space',
            'temp_min_c',
            'temp_max_c',
            'max_load',
        ]


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            'Пример запроса на создание партии товара',
            description='Базовый запрос',
            value={
                'product': 1,
                'supply_product_lot': 5,
                'manufacture_date': '2024-01-15',
                'expiry_date': '2024-02-15',
            },
            request_only=True,
        ),
    ],
)
class InventoryLotRequestSerializer(serializers.ModelSerializer):
    """Сериализатор запроса для создания/обновления InventoryLot"""

    class Meta:
        model = InventoryLot
        fields = [
            'product',
            'supply_product_lot',
            'manufacture_date',
            'expiry_date',
        ]


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            'Пример запроса на создание продукта',
            description='Базовый запрос',
            value={
                'unit': 1,
                'category': 2,
                'name': 'Молоко пастеризованное',
                'description': 'Молоко 3.2% жирности',
                'expiration_days': 14,
                'producer_name': 'ОАО "Молочный завод №1"',
                'producer_code': '12345678-1234-1234-1234-123456789012',
                'country_name': 'Россия',
                'additional_info': 'Упаковка: тетрапак, 1 литр'
            },
            request_only=True,
        ),
    ],
)
class ProductRequestSerializer(serializers.ModelSerializer):
    """Сериализатор запроса для создания/обновления Product"""

    class Meta:
        model = Product
        fields = [
            'unit',
            'category',
            'name',
            'description',
            'expiration_days',
            'producer_name',
            'producer_code',
            'country_name',
            'additional_info'
        ]


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            'Пример запроса на создание единицы измерения',
            description='Базовый запрос',
            value={
                'name': 'Килограмм',
            },
            request_only=True,
        ),
    ],
)
class ProductUnitRequestSerializer(serializers.ModelSerializer):
    """Сериализатор запроса для создания/обновления ProductUnit"""

    class Meta:
        model = ProductUnit
        fields = ['name']


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            'Пример запроса на создание категории продукта',
            description='Базовый запрос',
            value={
                'name': 'Молочные продукты',
            },
            request_only=True,
        ),
    ],
)
class ProductCategoryRequestSerializer(serializers.ModelSerializer):
    """Сериализатор запроса для создания/обновления ProductCategory"""

    class Meta:
        model = ProductCategory
        fields = ['name']


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            'Пример запроса на создание причины списания',
            description='Базовый запрос',
            value={
                'name': 'Истечение срока годности',
                'is_active': True,
                'requires_photo': False,
            },
            request_only=True,
        ),
    ],
)
class WriteoffReasonRequestSerializer(serializers.ModelSerializer):
    """Сериализатор запроса для создания/обновления WriteoffReason"""

    class Meta:
        model = WriteoffReason
        fields = ['name', 'is_active', 'requires_photo']


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            'Пример запроса на создание типа инвентаризации',
            description='Базовый запрос',
            value={
                'name': 'Плановая инвентаризация',
                'is_active': True,
            },
            request_only=True,
        ),
    ],
)
class StockTakeTypeRequestSerializer(serializers.ModelSerializer):
    """Сериализатор запроса для создания/обновления StockTakeType"""

    class Meta:
        model = StockTakeType
        fields = ['name', 'is_active']


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            'Пример запроса на создание причины стоп-листа',
            description='Базовый запрос',
            value={
                'name': 'Отсутствует в наличии',
            },
            request_only=True,
        ),
    ],
)
class StopListReasonRequestSerializer(serializers.ModelSerializer):
    """Сериализатор запроса для создания/обновления StopListReason"""

    class Meta:
        model = StopListReason
        fields = ['name']


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            'Пример запроса на создание типа оплаты',
            description='Базовый запрос',
            value={
                'name': 'Банковская карта',
            },
            request_only=True,
        ),
    ],
)
class PaymentMethodRequestSerializer(serializers.ModelSerializer):
    """Сериализатор запроса для создания/обновления PaymentMethod"""

    class Meta:
        model = PaymentMethod
        fields = ['name']


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            'Пример запроса на создание типа скидки в купоне',
            description='Базовый запрос',
            value={
                'name': 'Процентная скидка',
            },
            request_only=True,
        ),
    ],
)
class CouponDiscountTypeRequestSerializer(serializers.ModelSerializer):
    """Сериализатор запроса для создания/обновления CouponDiscountType"""

    class Meta:
        model = CouponDiscountType
        fields = ['name']


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            'Пример запроса на создание основания прайс-листа',
            description='Базовый запрос',
            value={
                'name': 'Себестоимость',
                'is_active': True,
            },
            request_only=True,
        ),
    ],
)
class PriceListBaseRequestSerializer(serializers.ModelSerializer):
    """Сериализатор запроса для создания/обновления PriceListBase"""

    class Meta:
        model = PriceListBase
        fields = ['name', 'is_active']


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            'Пример запроса на создание типа прайс-листа',
            description='Базовый запрос',
            value={
                'name': 'Оптовый прайс',
            },
            request_only=True,
        ),
    ],
)
class PriceListTypeRequestSerializer(serializers.ModelSerializer):
    """Сериализатор запроса для создания/обновления PriceListType"""

    class Meta:
        model = PriceListType
        fields = ['name']


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            'Пример запроса на создание типа перемещения',
            description='Базовый запрос',
            value={
                'name': 'Перемещение между складами',
            },
            request_only=True,
        ),
    ],
)
class MovementTypeRequestSerializer(serializers.ModelSerializer):
    """Сериализатор запроса для создания/обновления MovementType"""

    class Meta:
        model = MovementType
        fields = ['name']


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            'Пример запроса на создание типа места хранения',
            description='Базовый запрос',
            value={
                'name': 'Паллета',
            },
            request_only=True,
        ),
    ],
)
class SpaceTypeRequestSerializer(serializers.ModelSerializer):
    """Сериализатор запроса для создания/обновления SpaceType"""

    class Meta:
        model = SpaceType
        fields = ['name']


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            'Пример запроса на создание типа хранилища',
            description='Базовый запрос',
            value={
                'name': 'Холодильная камера',
            },
            request_only=True,
        ),
    ],
)
class StorageTypeRequestSerializer(serializers.ModelSerializer):
    """Сериализатор запроса для создания/обновления StorageType"""

    class Meta:
        model = StorageType
        fields = ['name']


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            'Пример запроса на создание условия хранения',
            description='Базовый запрос',
            value={
                'product': 1,
                'weight': 10,
                'temp_min_c': 2,
                'temp_max_c': 6,
                'light_sensitive': True,
            },
            request_only=True,
        ),
    ],
)
class StorageProfileRequestSerializer(serializers.ModelSerializer):
    """Сериализатор запроса для создания/обновления StorageProfile"""

    class Meta:
        model = StorageProfile
        fields = [
            'product',
            'weight',
            'temp_min_c',
            'temp_max_c',
            'light_sensitive',
        ]


@extend_schema_serializer(
    many=True,
    examples=[
        OpenApiExample(
            'Пример ответа от сервера',
            description='Базовый ответ',
            value=[
                {
                    'id': 1,
                    'name': 'Банковская карта',
                },
                {
                    'id': 2,
                    'name': 'Наличные',
                },
            ],
        ),
    ],
)
class PaymentMethodResponseSerializer(serializers.ModelSerializer):
    """Сериализатор ответа для PaymentMethod"""

    class Meta:
        model = PaymentMethod
        fields = ['id', 'name']


@extend_schema_serializer(
    many=True,
    examples=[
        OpenApiExample(
            'Пример ответа от сервера',
            description='Базовый ответ',
            value=[
                {
                    'id': 1,
                    'name': 'Отсутствует в наличии',
                },
                {
                    'id': 2,
                    'name': 'Истек срок годности',
                },
            ],
        ),
    ],
)
class StopListReasonResponseSerializer(serializers.ModelSerializer):
    """Сериализатор ответа для StopListReason"""

    class Meta:
        model = StopListReason
        fields = ['id', 'name']


@extend_schema_serializer(
    many=True,
    examples=[
        OpenApiExample(
            'Пример ответа от сервера',
            description='Базовый ответ',
            value=[
                {
                    'id': 1,
                    'name': 'Плановая инвентаризация',
                    'is_active': True,
                },
                {
                    'id': 2,
                    'name': 'Внеплановая инвентаризация',
                    'is_active': False,
                },
            ],
        ),
    ],
)
class StockTakeTypeResponseSerializer(serializers.ModelSerializer):
    """Сериализатор ответа для StockTakeType"""

    class Meta:
        model = StockTakeType
        fields = ['id', 'name', 'is_active']


@extend_schema_serializer(
    many=True,
    examples=[
        OpenApiExample(
            'Пример ответа от сервера',
            description='Базовый ответ',
            value=[
                {
                    'id': 1,
                    'name': 'Истечение срока годности',
                    'is_active': True,
                    'requires_photo': False,
                },
                {
                    'id': 2,
                    'name': 'Брак',
                    'is_active': True,
                    'requires_photo': True,
                },
            ],
        ),
    ],
)
class WriteoffReasonResponseSerializer(serializers.ModelSerializer):
    """Сериализатор ответа для WriteoffReason"""

    class Meta:
        model = WriteoffReason
        fields = ['id', 'name', 'is_active', 'requires_photo']


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            'Пример запроса на создание баланса инвентаря',
            description='Базовый запрос',
            value={
                'inventory_lot': 1,
                'storage': 2,
                'space': 3,
                'quantity': 100,
            },
            request_only=True,
        ),
    ],
)
class InventoryBalanceRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryBalance
        fields = ['inventory_lot', 'storage', 'space', 'quantity']


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            'Пример запроса на создание перемещения инвентаря',
            description='Базовый запрос',
            value={
                'inventory_lot': 1,
                'storage': 2,
                'space_from': 3,
                'space_to': 4,
                'created_by': 5,
                'movement_type': 6,
                'supply': 7,
                'sales_receipt': 8,
                'writeoff_act': 9,
                'quantity': 50,
            },
            request_only=True,
        ),
    ],
)
class InventoryMovementRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryMovement
        fields = [
            'inventory_lot',
            'storage',
            'space_from',
            'space_to',
            'created_by',
            'movement_type',
            'supply',
            'sales_receipt',
            'writeoff_act',
            'quantity',
        ]


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            'Пример запроса на создание прайс-листа',
            description='Базовый запрос',
            value={
                'storage': 1,
                'received_at': '2024-01-15T10:30:00Z',
                'business_date': '2024-01-15',
                'status': 'received',
            },
            request_only=True,
        ),
    ],
)
class PriceListRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceList
        fields = ['storage', 'received_at', 'business_date', 'status']


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            'Пример запроса на создание продукта прайс-листа',
            description='Базовый запрос',
            value={
                'price_list': 1,
                'price_list_type': 2,
                'product': 3,
                'price_list_base': 4,
                'input_cost_vh': 100,
                'final_price': 150,
                'regular_price': 120,
            },
            request_only=True,
        ),
    ],
)
class PriceListProductRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceListProduct
        fields = [
            'price_list',
            'price_list_type',
            'product',
            'price_list_base',
            'input_cost_vh',
            'final_price',
            'regular_price',
        ]


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            'Пример запроса на создание ограничения ценообразования',
            description='Базовый запрос',
            value={
                'storage': 1,
                'product_category': 2,
                'product': 3,
                'is_active': True,
                'scope': 'storage',
                'priority': 1,
                'max_daily_change_pct': 90,
                'max_markup_pct': 1000,
            },
            request_only=True,
        ),
    ],
)
class PricingConstraintRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PricingConstraint
        fields = [
            'storage',
            'product_category',
            'product',
            'is_active',
            'scope',
            'priority',
            'max_daily_change_pct',
            'max_markup_pct',
        ]


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            'Пример запроса на создание запуска ценообразования',
            description='Базовый запрос',
            value={
                'storage': 1,
                'created_by': 2,
                'status': 'started',
                'business_date': '2024-01-15',
                'started_at': '2024-01-15T10:30:00Z',
                'finished_at': '2024-01-15T11:30:00Z',
                'confirmed_at': '2024-01-15T12:00:00Z',
                'error_message': '',
            },
            request_only=True,
        ),
    ],
)
class PricingRunRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PricingRun
        fields = [
            'storage',
            'created_by',
            'status',
            'business_date',
            'started_at',
            'finished_at',
            'confirmed_at',
            'error_message',
        ]


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            'Пример запроса на создание цены магазина',
            description='Базовый запрос',
            value={
                'pricing_run': 1,
                'product': 2,
                'business_date': '2024-01-15',
                'price_list_type': 3,
                'price_list_base': 4,
                'final_price': 150,
                'is_sale_allowed': True,
                'block_reason': '',
            },
            request_only=True,
        ),
    ],
)
class StorePriceRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = StorePrice
        fields = [
            'pricing_run',
            'product',
            'business_date',
            'price_list_type',
            'price_list_base',
            'final_price',
            'is_sale_allowed',
            'block_reason',
        ]


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            'Пример запроса на создание купона',
            description='Базовый запрос',
            value={
                'storage': 1,
                'product': 2,
                'discount_type': 3,
                'value': 15,
                'valid_from': '2024-01-15',
                'valid_to': '2024-02-15',
                'min_quantity': 2,
                'is_active': True,
            },
            request_only=True,
        ),
    ],
)
class CouponRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = [
            'storage',
            'product',
            'discount_type',
            'value',
            'valid_from',
            'valid_to',
            'min_quantity',
            'is_active',
        ]


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            'Пример запроса на создание чека продажи',
            description='Базовый запрос',
            value={
                'storage': 1,
                'cashier': 2,
                'time_session': 3,
                'payment_method': 4,
                'status': 'draft',
                'opened_at': '2024-01-15T10:30:00Z',
                'closed_at': '2024-01-15T10:45:00Z',
                'total_gross': 500,
                'total_discount': 50,
                'total_payable': 450,
                'paid_amount': 450,
                'paid_at': '2024-01-15T10:45:00Z',
            },
            request_only=True,
        ),
    ],
)
class SaleReceiptRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleReceipt
        fields = [
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
        ]


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            'Пример запроса на создание строки чека',
            description='Базовый запрос',
            value={
                'sale_receipt': 1,
                'inventory_lot': 2,
                'coupon': 3,
                'price_list_type': 4,
                'price_list_base': 5,
                'quantity': 2,
                'unit_price': 150,
                'line_discount': 15,
                'line_total': 285,
            },
            request_only=True,
        ),
    ],
)
class SalesReceiptLineRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesReceiptLine
        fields = [
            'sale_receipt',
            'inventory_lot',
            'coupon',
            'price_list_type',
            'price_list_base',
            'quantity',
            'unit_price',
            'line_discount',
            'line_total',
        ]


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            'Пример запроса на создание стоп-листа',
            description='Базовый запрос',
            value={
                'storage': 1,
                'pricing_run': 2,
                'created_by': 3,
                'business_date': '2024-01-15',
                'status': 'draft',
                'sent_to_hq_at': '2024-01-15T10:30:00Z',
                'hq_comment': '',
                'closed_at': '2024-01-15T11:30:00Z',
            },
            request_only=True,
        ),
    ],
)
class StopListRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = StopList
        fields = [
            'storage',
            'pricing_run',
            'created_by',
            'business_date',
            'status',
            'sent_to_hq_at',
            'hq_comment',
            'closed_at',
        ]


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            'Пример запроса на создание продукта в стоп-листе',
            description='Базовый запрос',
            value={
                'stop_list': 1,
                'product': 2,
                'price_list_type': 3,
                'price_list_base': 4,
                'stop_list_reason': 5,
                'status': 'open',
                'input_cost_vh': 100,
                'yesterday_price': 150,
                'candidate_price': 140,
                'final_price_applied': 145,
            },
            request_only=True,
        ),
    ],
)
class StopListProductRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = StopListProduct
        fields = [
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
        ]


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            'Пример запроса на создание инвентаризации',
            description='Базовый запрос',
            value={
                'storage': 1,
                'space': 2,
                'stocktake_type': 3,
                'created_by': 4,
                'reviewed_by': 5,
                'status': 'draft',
                'business_date': '2024-01-15',
                'snapshot_at': '2024-01-15T10:30:00Z',
                'approved_at': '2024-01-15T11:30:00Z',
                'director_comment': '',
                'reviewed_at': '2024-01-15T12:00:00Z',
                'reviewer_comment': '',
                'closed_at': '2024-01-15T13:00:00Z',
            },
            request_only=True,
        ),
    ],
)
class StockTakeRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockTake
        fields = [
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
        ]


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            'Пример запроса на создание строки инвентаризации',
            description='Базовый запрос',
            value={
                'stocktake': 1,
                'space': 2,
                'inventory_lot': 3,
                'counted_by': 4,
                'counted_at': '2024-01-15T10:30:00Z',
                'quantity_expected': 100,
                'quantity_actual': 95,
                'is_expired': False,
                'comment': '',
            },
            request_only=True,
        ),
    ],
)
class StockTakeLineRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockTakeLine
        fields = [
            'stocktake',
            'space',
            'inventory_lot',
            'counted_by',
            'counted_at',
            'quantity_expected',
            'quantity_actual',
            'is_expired',
            'comment',
        ]


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            'Пример запроса на создание корректировки инвентаризации',
            description='Базовый запрос',
            value={
                'stocktake': 1,
                'stocktake_line': 2,
                'inventory_movement': 3,
            },
            request_only=True,
        ),
    ],
)
class StockTakeAdjustmentRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockTakeAdjustment
        fields = ['stocktake', 'stocktake_line', 'inventory_movement']


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            'Пример запроса на создание акта списания',
            description='Базовый запрос',
            value={
                'storage': 1,
                'writeoff_reason': 2,
                'created_by': 3,
                'reviewed_by': 4,
                'status': 'draft',
                'submitted_at': '2024-01-15T10:30:00Z',
                'submit_comment': '',
                'reviewed_at': '2024-01-15T11:30:00Z',
                'review_comment': '',
                'approved_at': '2024-01-15T12:00:00Z',
                'posted_at': '2024-01-15T13:00:00Z',
            },
            request_only=True,
        ),
    ],
)
class WriteOffActRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = WriteOffAct
        fields = [
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
        ]


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            'Пример запроса на создание строки списания',
            description='Базовый запрос',
            value={
                'writeoff_act': 1,
                'space': 2,
                'inventory_lot': 3,
                'quantity': 10,
                'comment': 'Истек срок годности',
            },
            request_only=True,
        ),
    ],
)
class WriteoffLineRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = WriteoffLine
        fields = ['writeoff_act', 'space', 'inventory_lot', 'quantity', 'comment']


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            'Пример запроса на создание вложения списания',
            description='Базовый запрос',
            value={
                'writeoff_act': 1,
                'image': 'string',
            },
            request_only=True,
        ),
    ],
)
class WriteoffAttachmentRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = WriteoffAttachment
        fields = ['writeoff_act', 'image']


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            'Пример запроса на создание проводки списания',
            description='Базовый запрос',
            value={
                'writeoff_act': 1,
                'writeoff_line': 2,
                'inventory_movement': 3,
            },
            request_only=True,
        ),
    ],
)
class WriteoffPostingRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = WriteoffPosting
        fields = ['writeoff_act', 'writeoff_line', 'inventory_movement']


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            'Пример запроса на создание партии товара',
            description='Базовый запрос',
            value={
                'product': 1,
                'supply_product': 5,
                'manufacture_date': '2024-01-15',
                'expiry_date': '2024-02-15',
                'barcode': '550e8400-e29b-41d4-a716-446655440000',
            },
            request_only=True,
        ),
    ],
)
class ProductInventoryLotRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInventoryLot
        fields = ['product', 'supply_product', 'manufacture_date', 'expiry_date', 'barcode']
