from django.urls import path

from ml_service.views import MlServiceHealthCheck, GetPredictionData

urlpatterns = [
    path('healthcheck', MlServiceHealthCheck.as_view(), name='ml_service_healthcheck'),
    path('predict', GetPredictionData.as_view(), name='predict'),
]
