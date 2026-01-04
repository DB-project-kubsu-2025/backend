from django.contrib import admin

from shops.models import (
    ProductUnit,
    ProductCategory,
    Product,
    StorageProfile,
    ProductMedia,
    StorageType,
    Storage,
)

@admin.register(ProductUnit)
class ProductUnitAdmin(admin.ModelAdmin):
    """Админ для ProductUnit"""

    list_display = ['id', 'name']


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    """Админ для ProductCategory"""

    list_display = ['id', 'name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Админ для Product"""

    list_display = ['id', 'name', 'unit', 'category', 'expiration_days', 'producer_name', 'country_name']
    raw_id_fields = ['category', 'unit']
    list_filter = ['category', 'unit']


@admin.register(StorageProfile)
class StorageProfileAdmin(admin.ModelAdmin):
    """Админ для StorageProfile"""

    list_display = ['id', 'product', 'weight', 'temp_min_c', 'temp_max_c', 'light_sensitive']
    raw_id_fields = ['product']


@admin.register(ProductMedia)
class ProductMediaAdmin(admin.ModelAdmin):
    """Админ для ProductMedia"""

    list_display = ['id', 'product']
    raw_id_fields = ['product']
    list_filter = ['product']


@admin.register(StorageType)
class StorageTypeAdmin(admin.ModelAdmin):
    """Админ для StorageType"""

    list_display = ['id', 'name']


@admin.register(Storage)
class StorageAdmin(admin.ModelAdmin):
    """Админ для Storage"""

    list_display = [
        'id',
        'director',
        'main_office_filial',
        'storage_type',
        'cadastral_number',
        'opened',
        'approved_by_main_company',
        'area',
    ]
    raw_id_fields = ['director', 'main_office_filial']
    list_filter = ['main_office_filial', 'opened']
