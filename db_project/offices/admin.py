from django.contrib import admin

from offices.models import (
    Region,
    City,
    MainOfficeFilial,
    StorageOpeningRequest,
)


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    """Админ для Region"""

    list_display = ['id', 'name']


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    """Админ для City"""

    list_display = ['id', 'name', 'region']
    raw_id_fields = ['region']
    list_filter = ['region']


@admin.register(MainOfficeFilial)
class MainOfficeFilialAdmin(admin.ModelAdmin):
    """Админ для MainOfficeFilial"""

    list_display = ['id', 'city', 'director', 'address', 'cadastral_number']
    raw_id_fields = ['city', 'director']
    list_filter = ['city', 'director']


@admin.register(StorageOpeningRequest)
class StorageOpeningRequestAdmin(admin.ModelAdmin):
    """Админ для StorageOpeningRequest"""

    list_display = ['id', 'storage', 'main_office_filial', 'is_confirmed', 'confirmed_by', 'confirmation_date']
    raw_id_fields = ['storage', 'main_office_filial', 'confirmed_by']
    list_filter = ['main_office_filial', 'confirmed_by']
