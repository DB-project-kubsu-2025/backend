from drf_spectacular.utils import OpenApiExample, extend_schema_serializer
from rest_framework import serializers
from shops.models import Space, InventoryLot, Storage, ProductMedia, Product, ProductUnit, ProductCategory, \
    WriteoffReason, StockTakeType, StopListReason, PaymentMethod, CouponDiscountType, PriceListBase, PriceListType, \
    MovementType, SpaceType, StorageType, StorageProfile


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
