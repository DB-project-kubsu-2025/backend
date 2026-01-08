from urllib.parse import urljoin

import requests
from django.conf import settings
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import status
from rest_framework.response import Response

from rest_framework.views import APIView

from common_utils.constants import DefaultAPIResponses, APISchemaTags


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
