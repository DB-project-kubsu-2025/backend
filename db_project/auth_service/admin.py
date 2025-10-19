from django.contrib import admin

from auth_service.models import Employee, Passport


@admin.register(Passport)
class PassportAdmin(admin.ModelAdmin):
    """Админ для модели Passport"""

    list_display = ['type', 'series', 'number', 'issue_date', 'issued_by', 'authority_code']
    list_display_links = ['series', 'number']

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    """Админ для модели Employee"""

    list_display = ['work_phone', 'last_name', 'first_name', 'second_name', 'username', 'date_joined']
    raw_id_fields = ['passport']
    readonly_fields = ['password']
