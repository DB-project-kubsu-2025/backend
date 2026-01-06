from drf_spectacular.utils import extend_schema_serializer, OpenApiExample
from rest_framework import serializers

from shops.models import (
    ProductUnit,
    ProductCategory, StorageType, SpaceType, MovementType, PriceListType, PriceListBase, CouponDiscountType,
    PaymentMethod, StopListReason, StockTakeType, WriteoffReason,
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
