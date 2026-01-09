from drf_spectacular.utils import OpenApiExample, extend_schema_serializer
from rest_framework import serializers
from shops.models import Space, InventoryLot, Storage, ProductMedia, Product


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
