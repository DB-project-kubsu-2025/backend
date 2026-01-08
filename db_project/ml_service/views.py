from dataclasses import asdict
from urllib.parse import urljoin

import requests
from django.conf import settings
from django.db.models import Sum
from django.db.models.functions import TruncDate
from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter, OpenApiExample
from rest_framework import status
from rest_framework.response import Response

from rest_framework.views import APIView

from common_utils.constants import DefaultAPIResponses, APISchemaTags
from ml_service.constants import PredictionType
from ml_service.selectors import get_data_for_prediction
from ml_service.serializers import PredictionDataRequestSerializer
from shops.models import ProductCategory, Storage, SaleReceipt, SalesReceiptLine


@extend_schema_view(
    get=extend_schema(
        'Проверить доступность ml_service',
        tags=[APISchemaTags.ML_SERVICE],
        responses={
            status.HTTP_200_OK: {},
            **DefaultAPIResponses.RESPONSES,
        },
    ),
)
class MlServiceHealthCheck(APIView):
    """Проверка доступности ml_service"""

    @staticmethod
    def get(request):
        """GET-запрос"""
        try:
            response = requests.get(
                urljoin(settings.ML_SERVICE_URL, 'healthcheck'),
            )
        except requests.exceptions.ConnectionError:
            return Response(status=status.HTTP_503_SERVICE_UNAVAILABLE)

        return Response(status=response.status_code)


@extend_schema_view(
    get=extend_schema(
        'Проверить доступность ml_service',
        tags=[APISchemaTags.ML_SERVICE],
        responses={
            status.HTTP_200_OK: {},
            **DefaultAPIResponses.RESPONSES,
        },
        parameters=[
            OpenApiParameter(
                name='prediction_type',
                description='Тип прогнозирования',
                required=True,
                type=str,
                location=OpenApiParameter.QUERY,
                examples=[
                    OpenApiExample(
                        'Прогнозирование по одной категории',
                        value=PredictionType.ONE_CATEGORY,
                        description='Прогнозирование по одной категории',
                    ),
                    OpenApiExample(
                        'Пакетное прогнозирование',
                        value=PredictionType.PACKAGE,
                        description='Пакетное прогнозирование',
                    ),
                ],
            ),
            OpenApiParameter(
                name='shop_id',
                description='ID хранилища',
                required=True,
                type=int,
                location=OpenApiParameter.QUERY,
            ),
            OpenApiParameter(
                name='forecast_days',
                description='На сколько дней предсказать',
                required=True,
                type=int,
                location=OpenApiParameter.QUERY,
                examples=[
                    OpenApiExample(
                        'Прогнозирование на 7 дней',
                        value=7,
                        description='Прогнозирование на 7 дней',
                    ),
                    OpenApiExample(
                        'Прогнозирование на 14 дней',
                        value=14,
                        description='Прогнозирование на 14 дней',
                    ),
                    OpenApiExample(
                        'Прогнозирование на 28 дней',
                        value=28,
                        description='Прогнозирование на 28 дней',
                    ),
                ],
            ),
            OpenApiParameter(
                name='product_category',
                description='Категория товара, если выбрано пакетное прогнозирование, игнорируется)',
                required=True,
                type=str,
                location=OpenApiParameter.QUERY,
                examples=[
                    OpenApiExample(
                        'FOODS',
                        value=ProductCategory.FOODS,
                        description='Прогнозирование на 7 дней',
                    ),
                    OpenApiExample(
                        'HOBBIES',
                        value=ProductCategory.HOBBIES,
                        description='HOBBIES',
                    ),
                    OpenApiExample(
                        'HOUSEHOLD',
                        value=ProductCategory.HOUSEHOLD,
                        description='HOBBIES',
                    ),
                ],
            ),
        ],
    ),
)
class GetPredictionData(APIView):
    """Хук получения результатов прогнозирования"""

    @staticmethod
    def get(request):
        """GET-запрос"""
        prediction_type = request.query_params.get('prediction_type')
        shop_id = request.query_params.get('shop_id')
        forecast_days = request.query_params.get('forecast_days')
        product_category = request.query_params.get('product_category')
        request_serializer = PredictionDataRequestSerializer(
            data={
                'prediction_type': prediction_type,
                'shop_id': shop_id,
                'forecast_days': forecast_days,
                'product_category': product_category,
            },
        )
        request_serializer.is_valid(raise_exception=True)

        storage = Storage.objects.get(id=shop_id)

        if prediction_type == PredictionType.ONE_CATEGORY:
            category_store_id = f'{product_category}/{storage.ml_service_id}'

            historical_data = asdict(get_data_for_prediction(product_category))
            if not historical_data:
                return Response(status=status.HTTP_204_NO_CONTENT)

            payload = {
                'category_store_id': category_store_id,
                'historical_data': historical_data,
                'forecast_days': forecast_days,
            }

            response = requests.post(
                urljoin(settings.ML_SERVICE_URL, '/prediction/one_category/'),
                data=payload,
            )
            return Response(status=status.HTTP_200_OK, data=response.json())
        elif prediction_type == PredictionType.PACKAGE:
            payload = {
                'data_for_prediction_items': [],
            }
            for _product_category in ProductCategory.CHOICES.keys():
                category_store_id = f'{_product_category}/{storage.ml_service_id}'
                historical_data = asdict(get_data_for_prediction(_product_category))

                payload['data_for_prediction_items'].append(
                    {
                        'category_store_id': category_store_id,
                        'historical_data': historical_data,
                        'forecast_days': forecast_days,
                    }
                )
            response = requests.get(
                urljoin(settings.ML_SERVICE_URL, '/prediction/package/'),
                data=payload,
            )
            return Response(status=status.HTTP_200_OK, data=response.json())

        return Response(status=status.HTTP_400_BAD_REQUEST)
