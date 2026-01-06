from drf_spectacular.utils import OpenApiExample, extend_schema_serializer
from rest_framework import serializers
from shops.models import Space


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
