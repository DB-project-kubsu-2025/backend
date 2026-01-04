from django.contrib import admin

from supplies.models import (
    Supplier,
    SupplierContact,
    SupplyContract,
    SupplyContractProduct,
    Supply,
    SupplyProduct,
    SupplyProductLot,
    DiscrepancyReason,
    SupplyDiscrepancy,
    DiscrepancyAttachment,
)

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    """Админ для модели Supplier"""

    list_display = ['name', 'ogrn', 'inn', 'kpp', 'bank_name', 'bik', 'corr_account']


@admin.register(SupplierContact)
class SupplierContactAdmin(admin.ModelAdmin):
    """Админ для модели SupplierContact"""

    list_display = ['supplier', 'surname', 'first_name', 'second_name', 'phone', 'email']
    raw_id_fields = ['supplier', 'passport']
    list_filter = ['supplier']


@admin.register(SupplyContract)
class SupplyContractAdmin(admin.ModelAdmin):
    """Админ для модели SupplyContract"""

    list_display = [
        'id',
        'supplier',
        'storage',
        'employee_entered_contract',
        'supplier_contact',
        'is_active',
        'expiration_date',
    ]
    raw_id_fields = ['supplier', 'storage', 'employee_entered_contract', 'supplier_contact']
    list_filter = ['supplier', 'storage', 'employee_entered_contract', 'supplier_contact']


@admin.register(SupplyContractProduct)
class SupplyContractProductAdmin(admin.ModelAdmin):
    """Админ для модели SupplyContractProduct"""

    list_display = ['id', 'supply_contract', 'product', 'price', 'quantity', 'delivery_frequency']
    raw_id_fields = ['supply_contract', 'product']


@admin.register(Supply)
class SupplyAdmin(admin.ModelAdmin):
    """Админ для модели Supply"""

    list_display = ['id', 'storage', 'supply_contract', 'created_by', 'received_by', 'planned_date', 'status']
    raw_id_fields = ['storage', 'supply_contract', 'created_by', 'received_by']
    list_filter = ['storage', 'supply_contract']


@admin.register(SupplyProduct)
class SupplyProductAdmin(admin.ModelAdmin):
    """Админ для модели SupplyProduct"""

    list_display = [
        'supply',
        'product',
        'supply_contract_product',
        'quantity_actual_total',
        'quantity_expected',
        'status',
        'purchase_price',
    ]
    raw_id_fields = ['supply', 'product', 'supply_contract_product']
    list_filter = ['supply', 'status']


@admin.register(SupplyProductLot)
class SupplyProductLotAdmin(admin.ModelAdmin):
    """Админ для модели SupplyProductLot"""

    list_display = [
        'id',
        'supply_product',
        'manufacture_date',
        'expiry_date_actual',
        'quantity_actual',
        'packaging_condition',
        'status',
    ]
    raw_id_fields = ['supply_product']
    list_filter = ['supply_product', 'status']


@admin.register(DiscrepancyReason)
class DiscrepancyReasonAdmin(admin.ModelAdmin):
    """Админ для модели DiscrepancyReason"""

    list_display = ['id', 'name']


@admin.register(SupplyDiscrepancy)
class SupplyDiscrepancyAdmin(admin.ModelAdmin):
    """Админ для модели SupplyDiscrepancy"""

    list_display = ['id', 'supply_product_lot', 'discrepancy_reason', 'created_by', 'decided_by', 'status']
    raw_id_fields = ['supply_product_lot', 'created_by', 'decided_by']
    list_filter = ['discrepancy_reason', 'status']


@admin.register(DiscrepancyAttachment)
class DiscrepancyAttachmentAdmin(admin.ModelAdmin):
    """Админ для модели DiscrepancyAttachment"""

    list_display = ['id', 'supply_discrepancy']
    raw_id_fields = ['supply_discrepancy']
    list_filter = ['supply_discrepancy']
