from django.urls import path

from auth_service.views import (
    HealthCheck,
    CustomTokenObtainPairView,
    CustomTokenRefreshView,
    ChangePassword,
    RegisterEmployee,
    LogOut,
    EmployeeChange,
)

urlpatterns = [
    path('healthcheck/', HealthCheck.as_view(), name='health_check'),
    path('token/obtain/', CustomTokenObtainPairView.as_view(), name='token_obtain'),
    path('employee/register/', RegisterEmployee.as_view(), name='employee_register'),
    path('employee/', EmployeeChange.as_view(), name='employee_change'),
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('password/change/', ChangePassword.as_view(), name='password_change'),
    path('logout/', LogOut.as_view(), name='log_out'),
]
