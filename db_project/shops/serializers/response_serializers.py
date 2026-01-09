from drf_spectacular.utils import extend_schema_serializer, OpenApiExample
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
    many=True,
    examples=[
        OpenApiExample(
            'Пример ответа от сервера',
            description='Базовый ответ',
            value=[
                {
                    'id': 1,
                    'storage': 2,
                    'space_type': 3,
                    'parent_space': 4,
                    'temp_min_c': 2,
                    'temp_max_c': 6,
                    'max_load': 100,
                },
                {
                    'id': 2,
                    'storage': 2,
                    'space_type': 5,
                    'parent_space': 1,
                    'temp_min_c': -5,
                    'temp_max_c': -2,
                    'max_load': 200,
                },
            ],
        ),
    ],
)
class SpaceResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Space
        fields = ['id', 'storage', 'space_type', 'parent_space', 'temp_min_c', 'temp_max_c', 'max_load']


@extend_schema_serializer(
    many=True,
    examples=[
        OpenApiExample(
            'Пример ответа от сервера',
            description='Базовый ответ',
            value=[
                {
                    'id': 1,
                    'product': 1,
                    'supply_product_lot': 5,
                    'manufacture_date': '2024-01-15',
                    'expiry_date': '2024-02-15',
                },
                {
                    'id': 2,
                    'product': 2,
                    'supply_product_lot': 6,
                    'manufacture_date': '2024-01-16',
                    'expiry_date': '2024-02-16',
                },
            ],
        ),
    ],
)
class InventoryLotResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryLot
        fields = ['id', 'product', 'supply_product_lot', 'manufacture_date', 'expiry_date']


@extend_schema_serializer(
    many=True,
    examples=[
        OpenApiExample(
            'Пример ответа от сервера',
            description='Базовый ответ',
            value=[
                {
                    'id': 1,
                    'director': 1,
                    'main_office_filial': 2,
                    'storage_type': 3,
                    'cadastral_number': '77:01:0001001:1001',
                    'approved_by_main_company': True,
                    'opened': True,
                    'area': 500,
                    'utilization_percent': 75,
                    'ml_service_id': 'storage_001',
                },
                {
                    'id': 2,
                    'director': 2,
                    'main_office_filial': 3,
                    'storage_type': 4,
                    'cadastral_number': '77:01:0001001:1002',
                    'approved_by_main_company': False,
                    'opened': True,
                    'area': 300,
                    'utilization_percent': 60,
                    'ml_service_id': 'storage_002',
                },
            ],
        ),
    ],
)
class StorageResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storage
        fields = [
            'id',
            'director',
            'main_office_filial',
            'storage_type',
            'cadastral_number',
            'approved_by_main_company',
            'opened',
            'area',
            'utilization_percent',
            'ml_service_id',
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
                    'product': 1,
                    'image': '/media/products/image1.jpg',
                },
                {
                    'id': 2,
                    'product': 1,
                    'image': '/media/products/image2.jpg',
                },
            ],
        ),
    ],
)
class ProductMediaResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductMedia
        fields = ['id', 'product', 'image']


@extend_schema_serializer(
    many=True,
    examples=[
        OpenApiExample(
            'Пример ответа от сервера',
            description='Базовый ответ',
            value=[
                {
                    'id': 1,
                    'name': 'шт',
                },
                {
                    'id': 2,
                    'name': 'кг',
                },
            ],
        ),
    ],
)
class ProductUnitResponseSerializer(serializers.ModelSerializer):
    """Сериализатор ответа для ProductUnit"""

    class Meta:
        model = ProductUnit
        fields = [
            'id',
            'name',
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
                    'name': 'Молочные продукты и яйца',
                },
                {
                    'id': 2,
                    'name': 'Мясо и мясные продукты',
                },
            ],
        ),
    ],
)
class ProductCategoryResponseSerializer(serializers.ModelSerializer):
    """Сериализатор ответа для ProductUnit"""

    class Meta:
        model = ProductCategory
        fields = [
            'id',
            'name',
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
                    'unit': 1,
                    'category': 2,
                    'name': 'Молоко 2.5%',
                    'description': 'Пастеризованное молоко',
                    'expiration_days': 5,
                    'producer_name': 'Молочный комбинат',
                    'producer_code': '550e8400-e29b-41d4-a716-446655440000',
                    'country_name': 'Россия',
                    'additional_info': 'В пластиковой бутылке',
                },
                {
                    'id': 2,
                    'unit': 2,
                    'category': 1,
                    'name': 'Хлеб пшеничный',
                    'description': 'Свежий хлеб',
                    'expiration_days': 3,
                    'producer_name': 'Хлебозавод №1',
                    'producer_code': '123e4567-e89b-12d3-a456-426614174000',
                    'country_name': 'Россия',
                    'additional_info': 'Нарезной',
                },
            ],
        ),
    ],
)
class ProductResponseSerializer(serializers.ModelSerializer):
    """Сериализатор ответа для Product"""

    class Meta:
        model = Product
        fields = [
            'id',
            'unit',
            'category',
            'name',
            'description',
            'expiration_days',
            'producer_name',
            'producer_code',
            'country_name',
            'additional_info',
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
                    'product': 1,
                    'weight': 1,
                    'temp_min_c': 2,
                    'temp_max_c': 6,
                    'light_sensitive': True,
                },
                {
                    'id': 2,
                    'product': 2,
                    'weight': 5,
                    'temp_min_c': -5,
                    'temp_max_c': -2,
                    'light_sensitive': False,
                },
            ],
        ),
    ],
)
class StorageProfileResponseSerializer(serializers.ModelSerializer):
    """Сериализатор ответа для StorageProfile"""

    class Meta:
        model = StorageProfile
        fields = [
            'id',
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
                    'name': 'Холодильная камера',
                },
                {
                    'id': 2,
                    'name': 'Морозильная камера',
                },
            ],
        ),
    ],
)
class StorageTypeResponseSerializer(serializers.ModelSerializer):
    """Сериализатор ответа для StorageType"""

    class Meta:
        model = StorageType
        fields = [
            'id',
            'name',
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
                    'name': 'Полка',
                },
                {
                    'id': 2,
                    'name': 'Ячейка',
                },
            ],
        ),
    ],
)
class SpaceTypeResponseSerializer(serializers.ModelSerializer):
    """Сериализатор ответа для SpaceType"""

    class Meta:
        model = SpaceType
        fields = [
            'id',
            'name',
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
                    'name': 'Поступление на склад',
                },
                {
                    'id': 2,
                    'name': 'Отгрузка со склада',
                },
            ],
        ),
    ],
)
class MovementTypeResponseSerializer(serializers.ModelSerializer):
    """Сериализатор ответа для MovementType"""

    class Meta:
        model = MovementType
        fields = [
            'id',
            'name',
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
                    'name': 'Розничный',
                },
                {
                    'id': 2,
                    'name': 'Оптовый',
                },
            ],
        ),
    ],
)
class PriceListTypeResponseSerializer(serializers.ModelSerializer):
    """Сериализатор ответа для PriceListType"""

    class Meta:
        model = PriceListType
        fields = [
            'id',
            'name',
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
                    'name': 'Закупочный прайс',
                },
                {
                    'id': 2,
                    'name': 'Себестоимость',
                },
            ],
        ),
    ],
)
class PriceListBaseResponseSerializer(serializers.ModelSerializer):
    """Сериализатор ответа для PriceListBase"""

    class Meta:
        model = PriceListBase
        fields = [
            'id',
            'name',
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
                    'name': 'Процентная скидка',
                },
                {
                    'id': 2,
                    'name': 'Фиксированная сумма',
                },
            ],
        ),
    ],
)
class CouponDiscountTypeResponseSerializer(serializers.ModelSerializer):
    """Сериализатор ответа для CouponDiscountType"""

    class Meta:
        model = CouponDiscountType
        fields = [
            'id',
            'name',
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
                    'name': 'Наличные',
                },
                {
                    'id': 2,
                    'name': 'Безналичный расчет',
                },
            ],
        ),
    ],
)
class PaymentMethodResponseSerializer(serializers.ModelSerializer):
    """Сериализатор ответа для PaymentMethod"""

    class Meta:
        model = PaymentMethod
        fields = [
            'id',
            'name',
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
        fields = [
            'id',
            'name',
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
                    'name': 'Плановая инвентаризация',
                },
                {
                    'id': 2,
                    'name': 'Внеплановая инвентаризация',
                },
            ],
        ),
    ],
)
class StockTakeTypeResponseSerializer(serializers.ModelSerializer):
    """Сериализатор ответа для StockTakeType"""

    class Meta:
        model = StockTakeType
        fields = [
            'id',
            'name',
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
                    'name': 'Брак',
                    'requires_photo': True,
                },
                {
                    'id': 2,
                    'name': 'Истечение срока годности',
                    'requires_photo': False,
                },
            ],
        ),
    ],
)
class WriteoffReasonResponseSerializer(serializers.ModelSerializer):
    """Сериализатор ответа для WriteoffReason"""

    class Meta:
        model = WriteoffReason
        fields = [
            'id',
            'name',
            'requires_photo',
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
                    'product': 1,
                    'supply_product': 5,
                    'manufacture_date': '2024-01-15',
                    'expiry_date': '2024-02-15',
                    'barcode': '550e8400-e29b-41d4-a716-446655440000',
                },
                {
                    'id': 2,
                    'product': 2,
                    'supply_product': 6,
                    'manufacture_date': '2024-01-16',
                    'expiry_date': '2024-02-16',
                    'barcode': '123e4567-e89b-12d3-a456-426614174000',
                },
            ],
        ),
    ],
)
class ProductInventoryLotResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInventoryLot
        fields = ['id', 'product', 'supply_product', 'manufacture_date', 'expiry_date', 'barcode']


@extend_schema_serializer(
    many=True,
    examples=[
        OpenApiExample(
            'Пример ответа от сервера',
            description='Базовый ответ',
            value=[
                {
                    'id': 1,
                    'inventory_lot': 1,
                    'storage': 2,
                    'space': 3,
                    'quantity': 100,
                },
                {
                    'id': 2,
                    'inventory_lot': 2,
                    'storage': 2,
                    'space': 4,
                    'quantity': 50,
                },
            ],
        ),
    ],
)
class InventoryBalanceResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryBalance
        fields = ['id', 'inventory_lot', 'storage', 'space', 'quantity']


@extend_schema_serializer(
    many=True,
    examples=[
        OpenApiExample(
            'Пример ответа от сервера',
            description='Базовый ответ',
            value=[
                {
                    'id': 1,
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
            ],
        ),
    ],
)
class InventoryMovementResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryMovement
        fields = [
            'id',
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
    many=True,
    examples=[
        OpenApiExample(
            'Пример ответа от сервера',
            description='Базовый ответ',
            value=[
                {
                    'id': 1,
                    'storage': 1,
                    'received_at': '2024-01-15T10:30:00Z',
                    'business_date': '2024-01-15',
                    'status': 'received',
                },
                {
                    'id': 2,
                    'storage': 2,
                    'received_at': '2024-01-16T11:00:00Z',
                    'business_date': '2024-01-16',
                    'status': 'validated',
                },
            ],
        ),
    ],
)
class PriceListResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceList
        fields = ['id', 'storage', 'received_at', 'business_date', 'status']


@extend_schema_serializer(
    many=True,
    examples=[
        OpenApiExample(
            'Пример ответа от сервера',
            description='Базовый ответ',
            value=[
                {
                    'id': 1,
                    'price_list': 1,
                    'price_list_type': 2,
                    'product': 3,
                    'price_list_base': 4,
                    'input_cost_vh': 100,
                    'final_price': 150,
                    'regular_price': 120,
                },
            ],
        ),
    ],
)
class PriceListProductResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceListProduct
        fields = [
            'id',
            'price_list',
            'price_list_type',
            'product',
            'price_list_base',
            'input_cost_vh',
            'final_price',
            'regular_price',
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
                    'storage': 1,
                    'product_category': 2,
                    'product': 3,
                    'is_active': True,
                    'scope': 'storage',
                    'priority': 1,
                    'max_daily_change_pct': 90,
                    'max_markup_pct': 1000,
                },
            ],
        ),
    ],
)
class PricingConstraintResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PricingConstraint
        fields = [
            'id',
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
    many=True,
    examples=[
        OpenApiExample(
            'Пример ответа от сервера',
            description='Базовый ответ',
            value=[
                {
                    'id': 1,
                    'storage': 1,
                    'created_by': 2,
                    'status': 'started',
                    'business_date': '2024-01-15',
                    'started_at': '2024-01-15T10:30:00Z',
                    'finished_at': '2024-01-15T11:30:00Z',
                    'confirmed_at': '2024-01-15T12:00:00Z',
                    'error_message': '',
                },
            ],
        ),
    ],
)
class PricingRunResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PricingRun
        fields = [
            'id',
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
    many=True,
    examples=[
        OpenApiExample(
            'Пример ответа от сервера',
            description='Базовый ответ',
            value=[
                {
                    'id': 1,
                    'pricing_run': 1,
                    'product': 2,
                    'business_date': '2024-01-15',
                    'price_list_type': 3,
                    'price_list_base': 4,
                    'final_price': 150,
                    'is_sale_allowed': True,
                    'block_reason': '',
                },
            ],
        ),
    ],
)
class StorePriceResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = StorePrice
        fields = [
            'id',
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
    many=True,
    examples=[
        OpenApiExample(
            'Пример ответа от сервера',
            description='Базовый ответ',
            value=[
                {
                    'id': 1,
                    'storage': 1,
                    'product': 2,
                    'discount_type': 3,
                    'value': 15,
                    'valid_from': '2024-01-15',
                    'valid_to': '2024-02-15',
                    'min_quantity': 2,
                    'is_active': True,
                },
            ],
        ),
    ],
)
class CouponResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = [
            'id',
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
    many=True,
    examples=[
        OpenApiExample(
            'Пример ответа от сервера',
            description='Базовый ответ',
            value=[
                {
                    'id': 1,
                    'storage': 1,
                    'cashier': 2,
                    'time_session': 3,
                    'payment_method': 4,
                    'status': 'paid',
                    'opened_at': '2024-01-15T10:30:00Z',
                    'closed_at': '2024-01-15T10:45:00Z',
                    'total_gross': 500,
                    'total_discount': 50,
                    'total_payable': 450,
                    'paid_amount': 450,
                    'paid_at': '2024-01-15T10:45:00Z',
                },
            ],
        ),
    ],
)
class SaleReceiptResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleReceipt
        fields = [
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
            ],
        ),
    ],
)
class SalesReceiptLineResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesReceiptLine
        fields = [
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
                    'storage': 1,
                    'pricing_run': 2,
                    'created_by': 3,
                    'business_date': '2024-01-15',
                    'status': 'confirmed',
                    'sent_to_hq_at': '2024-01-15T10:30:00Z',
                    'hq_comment': 'Одобрено',
                    'closed_at': '2024-01-15T11:30:00Z',
                },
            ],
        ),
    ],
)
class StopListResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = StopList
        fields = [
            'id',
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
    many=True,
    examples=[
        OpenApiExample(
            'Пример ответа от сервера',
            description='Базовый ответ',
            value=[
                {
                    'id': 1,
                    'stop_list': 1,
                    'product': 2,
                    'price_list_type': 3,
                    'price_list_base': 4,
                    'stop_list_reason': 5,
                    'status': 'resolved',
                    'input_cost_vh': 100,
                    'yesterday_price': 150,
                    'candidate_price': 140,
                    'final_price_applied': 145,
                },
            ],
        ),
    ],
)
class StopListProductResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = StopListProduct
        fields = [
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
                    'storage': 1,
                    'space': 2,
                    'stocktake_type': 3,
                    'created_by': 4,
                    'reviewed_by': 5,
                    'status': 'approved',
                    'business_date': '2024-01-15',
                    'snapshot_at': '2024-01-15T10:30:00Z',
                    'approved_at': '2024-01-15T11:30:00Z',
                    'director_comment': 'Все верно',
                    'reviewed_at': '2024-01-15T12:00:00Z',
                    'reviewer_comment': 'Проверено',
                    'closed_at': '2024-01-15T13:00:00Z',
                },
            ],
        ),
    ],
)
class StockTakeResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockTake
        fields = [
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
                    'stocktake': 1,
                    'space': 2,
                    'inventory_lot': 3,
                    'counted_by': 4,
                    'counted_at': '2024-01-15T10:30:00Z',
                    'quantity_expected': 100,
                    'quantity_actual': 95,
                    'is_expired': False,
                    'comment': 'Небольшое расхождение',
                },
            ],
        ),
    ],
)
class StockTakeLineResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockTakeLine
        fields = [
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
                    'stocktake': 1,
                    'stocktake_line': 2,
                    'inventory_movement': 3,
                },
            ],
        ),
    ],
)
class StockTakeAdjustmentResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockTakeAdjustment
        fields = ['id', 'stocktake', 'stocktake_line', 'inventory_movement']


@extend_schema_serializer(
    many=True,
    examples=[
        OpenApiExample(
            'Пример ответа от сервера',
            description='Базовый ответ',
            value=[
                {
                    'id': 1,
                    'storage': 1,
                    'writeoff_reason': 2,
                    'created_by': 3,
                    'reviewed_by': 4,
                    'status': 'posted',
                    'submitted_at': '2024-01-15T10:30:00Z',
                    'submit_comment': 'Отправлено на утверждение',
                    'reviewed_at': '2024-01-15T11:30:00Z',
                    'review_comment': 'Проверено',
                    'approved_at': '2024-01-15T12:00:00Z',
                    'posted_at': '2024-01-15T13:00:00Z',
                },
            ],
        ),
    ],
)
class WriteOffActResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = WriteOffAct
        fields = [
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
                    'writeoff_act': 1,
                    'space': 2,
                    'inventory_lot': 3,
                    'quantity': 10,
                    'comment': 'Истек срок годности',
                },
            ],
        ),
    ],
)
class WriteoffLineResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = WriteoffLine
        fields = ['id', 'writeoff_act', 'space', 'inventory_lot', 'quantity', 'comment']


@extend_schema_serializer(
    many=True,
    examples=[
        OpenApiExample(
            'Пример ответа от сервера',
            description='Базовый ответ',
            value=[
                {
                    'id': 1,
                    'writeoff_act': 1,
                    'image': '/media/writeoff_attachments/image1.jpg',
                },
            ],
        ),
    ],
)
class WriteoffAttachmentResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = WriteoffAttachment
        fields = ['id', 'writeoff_act', 'image']


@extend_schema_serializer(
    many=True,
    examples=[
        OpenApiExample(
            'Пример ответа от сервера',
            description='Базовый ответ',
            value=[
                {
                    'id': 1,
                    'writeoff_act': 1,
                    'writeoff_line': 2,
                    'inventory_movement': 3,
                },
            ],
        ),
    ],
)
class WriteoffPostingResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = WriteoffPosting
        fields = ['id', 'writeoff_act', 'writeoff_line', 'inventory_movement']
