from drf_spectacular.utils import extend_schema_serializer
from rest_framework import serializers


@extend_schema_serializer()
class GetPredictionDataWithOneCategoryResponseSerializer(serializers.Serializer):
    """Сериализатор ответа для хука прогнозирования спроса при выборе одной категории"""

    # todo: Допилить сериализаторы, добавить во View и в Swagger


@extend_schema_serializer()
class GetPredictionDataWithPackageResponseSerializer(serializers.Serializer):
    """Сериализатор ответа для хука прогнозирования спроса при пакетном прогнозировании"""

    # todo: Допилить сериализаторы, добавить во View и в Swagger
