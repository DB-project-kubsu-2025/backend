from rest_framework import serializers

class PredictionDataRequestSerializer(serializers.Serializer):
    """Сериализатор запроса для хука получения результатов прогнозирования"""

    prediction_type = serializers.CharField(help_text='Тип прогнозирования')
    shop_id = serializers.IntegerField(help_text='ID хранилища')
    forecast_days = serializers.IntegerField(help_text='Дни для прогнозирования')
    product_category = serializers.CharField(help_text='Категория продуктов')
