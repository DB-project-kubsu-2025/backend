from django.urls import path

from ml_service.views import MlServiceHealthCheck

urlpatterns = [
    path('healthcheck', MlServiceHealthCheck.as_view(), name='ml_service_healthcheck'),
]
