from django.urls import include, path
from rest_framework.routers import DefaultRouter

from employees.views.private import UserGroupsView
from employees.views.reference_books import (
    GetJobPosition,
    GetWorkingRate,
    GetWorkplace,
    GetEmployee,
    GetLeaveRequestType,
    GetTimeSessionCloseReason,
)
from employees.views.user_info import UserInfoHookAPIView

router = DefaultRouter()
router.register(r'job-positions', GetJobPosition, basename='job-position')
router.register(r'working-rates', GetWorkingRate, basename='working-rate')
router.register(r'workplaces', GetWorkplace, basename='workplace')
router.register(r'employees', GetEmployee, basename='employee')
router.register(r'leave-request-types', GetLeaveRequestType, basename='leave-request-type')
router.register(r'time-session-close-reasons', GetTimeSessionCloseReason, basename='time-session-close-reason')
urlpatterns = [
    path('', include(router.urls)),
    # user-info: без лишних слов
    path('user-info/', UserInfoHookAPIView.as_view(), name='user-info-self'),
    # Получить данные пользователя по pk (только для staff/superuser или самого пользователя)
    path('user-info/<int:pk>/', UserInfoHookAPIView.as_view(), name='user-info-detail'),
    path('user-groups', UserGroupsView.as_view(), name='user_groups'),
]
