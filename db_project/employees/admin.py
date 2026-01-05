from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from employees.models import (
    Passport,
    WorkingRate,
    JobPosition,
    Salary,
    Employee,
    LeaveRequestType,
    LeaveRequest,
    LeaveRequestAttachment,
    AnnualLeaveBalance,
    TimeEntry,
    TimeSessionCloseReason,
    TimeSession,
    TimeDay,
    GlobalTimePolicy,
)

@admin.register(Passport)
class PassportAdmin(admin.ModelAdmin):
    """Админ для модели Passport"""

    list_display = ['type', 'series', 'number', 'issue_date', 'issued_by', 'authority_code']
    list_display_links = ['series', 'number']


@admin.register(WorkingRate)
class WorkingRateAdmin(admin.ModelAdmin):
    """Админ для модели WorkingRate"""

    list_display = ['id', 'name', 'monthly_output']


@admin.register(JobPosition)
class JobPositionAdmin(admin.ModelAdmin):
    """Админ для модели JobPosition"""

    list_display = ['id', 'name']


@admin.register(Salary)
class SalaryAdmin(admin.ModelAdmin):
    """Админ для модели Salary"""

    list_display = ['amount', 'job_position', 'working_rate', 'dt_created', 'dt_updated']
    raw_id_fields = ['job_position', 'working_rate']


@admin.register(Employee)
class EmployeeAdmin(UserAdmin):
    """Админ для модели Employee"""
    model = Employee
    add_form = UserCreationForm
    form = UserChangeForm
    list_display = ['work_phone', 'last_name', 'first_name', 'second_name', 'username', 'date_joined']

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (
            'Personal info',
            {
                'fields': (
                    'last_name',
                    'first_name',
                    'second_name',
                    'gender',
                    'birth_date',
                    'work_phone',
                    'passport',
                    'snils',
                    'inn',
                    'workplace',
                ),
            },
        ),
        (
            'Permissions',
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions',
                ),
            },
        ),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {'fields': ('username', 'password1', 'password2')}),
        (
            'Personal info',
            {
                'fields': (
                    'last_name',
                    'first_name',
                    'second_name',
                    'gender',
                    'birth_date',
                    'work_phone',
                    'passport',
                    'snils',
                    'inn',
                    'workplace',
                ),
            },
        ),
        (
            'Permissions',
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions',
                ),
            },
        ),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )


@admin.register(LeaveRequestType)
class LeaveRequestTypeAdmin(admin.ModelAdmin):
    """Админ для модели LeaveRequestType"""

    list_display = ['name', 'counts_against_annual', 'requires_documents', 'documents_due_days']


@admin.register(LeaveRequest)
class LeaveRequestAdmin(admin.ModelAdmin):
    """Админ для модели LeaveRequest"""

    list_display = ['employee', 'approved_by', 'status', 'start_date', 'end_date', 'approved_at']
    raw_id_fields = ['employee', 'approved_by']
    list_filter = ['status']


@admin.register(LeaveRequestAttachment)
class LeaveRequestAttachmentAdmin(admin.ModelAdmin):
    """Админ для модели LeaveRequestAttachment"""

    list_display = ['leave_request', 'file']
    raw_id_fields = ['leave_request']


@admin.register(AnnualLeaveBalance)
class AnnualLeaveBalanceAdmin(admin.ModelAdmin):
    """Админ для модели LeaveRequestAttachment"""

    list_display = ['employee', 'year', 'base_days', 'carry_in_days', 'manual_adjust_days']
    raw_id_fields = ['employee']
    list_filter = ['employee', 'year']


@admin.register(GlobalTimePolicy)
class GlobalTimePolicyAdmin(admin.ModelAdmin):
    """Админ для модели GlobalTimePolicy"""

    list_display = ['required_minutes', 'cut_off_minute', 'prompt_wait_minutes', 'effective_from', 'effective_to']


@admin.register(TimeEntry)
class TimeEntryAdmin(admin.ModelAdmin):
    """Админ для модели TimeEntry"""

    list_display = ['employee', 'date', 'minutes', 'comment']
    list_filter = ['employee']
    raw_id_fields = ['employee']


@admin.register(TimeSessionCloseReason)
class TimeSessionCloseReasonAdmin(admin.ModelAdmin):
    """Админ для модели TimeSessionCloseReason"""

    list_display = ['id', 'name']


@admin.register(TimeSession)
class TimeSessionAdmin(admin.ModelAdmin):
    """Админ для модели TimeSession"""

    list_display = ['employee', 'close_reason', 'closed', 'login_at', 'logout_at']
    raw_id_fields = ['employee', 'close_reason']


@admin.register(TimeDay)
class TimeDayAdmin(admin.ModelAdmin):
    """Админ для модели TimeDay"""

    list_display = ['employee', 'date', 'comment', 'adjusted_minutes', 'adjustment_reason']
    raw_id_fields = ['employee', 'adjustment_reason']
