from django.urls import include, path
from rest_framework.routers import SimpleRouter

from employees.views.private import (
    PassportViewSet,
    WorkingRateViewSet,
    JobPositionViewSet,
    SalaryViewSet,
    WorkplaceViewSet,
    EmployeeViewSet,
    LeaveRequestTypeViewSet,
    LeaveRequestViewSet,
    LeaveRequestAttachmentViewSet,
    AnnualLeaveBalanceViewSet,
    TimeEntryViewSet,
    TimeSessionCloseReasonViewSet,
    TimeSessionViewSet,
    TimeDayViewSet,
    UserGroupsView,
)
from employees.views.user_info import UserInfoHookAPIView


router = SimpleRouter()

# --- Reference / directory-like models (CRUD) ---
router.register(r"passports", PassportViewSet, basename="passport")
router.register(r"working-rates", WorkingRateViewSet, basename="working-rate")
router.register(r"job-positions", JobPositionViewSet, basename="job-position")
router.register(r"salaries", SalaryViewSet, basename="salary")
router.register(r"workplaces", WorkplaceViewSet, basename="workplace")
router.register(r"employees", EmployeeViewSet, basename="employee")

# --- Leave requests (CRUD) ---
router.register(r"leave-request-types", LeaveRequestTypeViewSet, basename="leave-request-type")
router.register(r"leave-requests", LeaveRequestViewSet, basename="leave-request")
router.register(r"leave-request-attachments", LeaveRequestAttachmentViewSet, basename="leave-request-attachment")
router.register(r"annual-leave-balances", AnnualLeaveBalanceViewSet, basename="annual-leave-balance")

# --- Time tracking (CRUD) ---
router.register(r"time-entries", TimeEntryViewSet, basename="time-entry")
router.register(r"time-session-close-reasons", TimeSessionCloseReasonViewSet, basename="time-session-close-reason")
router.register(r"time-sessions", TimeSessionViewSet, basename="time-session")
router.register(r"time-days", TimeDayViewSet, basename="time-day")


urlpatterns = [
    path("", include(router.urls)),

    # user-info: без лишних слов
    path("user-info/", UserInfoHookAPIView.as_view(), name="user-info-self"),
    # Получить данные пользователя по pk (только для staff/superuser или самого пользователя)
    path("user-info/<int:pk>/", UserInfoHookAPIView.as_view(), name="user-info-detail"),

    path("user-groups", UserGroupsView.as_view(), name="user_groups"),
]