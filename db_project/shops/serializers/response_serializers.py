from drf_spectacular.utils import extend_schema_serializer, OpenApiExample
from rest_framework import serializers

from shops.models import (
    ProductUnit,
    ProductCategory,
    StorageType,
    SpaceType,
    MovementType,
    PriceListType,
    PriceListBase,
    CouponDiscountType,
    PaymentMethod,
    StopListReason,
    StockTakeType,
    WriteoffReason,
    Product, StorageProfile,
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
