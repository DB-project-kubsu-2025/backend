from drf_spectacular.utils import OpenApiExample, extend_schema_serializer
from rest_framework import serializers

from supplies.models import (
    Supplier, SupplierContact, SupplyContract, SupplyContractProduct,
    Supply, SupplyProduct, SupplyProductLot,
    DiscrepancyReason, SupplyDiscrepancy, DiscrepancyAttachment,
)


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            "Пример: создать поставщика",
            value={
                "name": "ООО Ромашка",
                "address": "г. Краснодар, ул. Пушкина, д. 1",
                "ogrn": "1234567890123",
                "inn": "123456789012",
                "kpp": "123456789",
                "bank_name": "Сбербанк",
                "bik": "044525225",
                "corr_account": "30101810400000000225",
                "checking_account": "40702810900000000001",
                "swift": "SABRRUMM",
                "iban": "RU00TESTIBAN000000000000000",
            },
            request_only=True,
        )
    ]
)
class SupplierRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = "__all__"
        read_only_fields = ["id", "dt_created", "dt_updated"]


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            "Пример: создать контактное лицо поставщика",
            value={
                "supplier": 1,
                "passport": 1,
                "surname": "Иванов",
                "first_name": "Иван",
                "second_name": "Иванович",
                "snils": "123-456-789 00",
                "inn": "123456789012",
                "phone": "+79990000000",
                "email": "ivanov@example.com",
                "job_title": "Менеджер",
            },
            request_only=True,
        )
    ]
)
class SupplierContactRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplierContact
        fields = "__all__"
        read_only_fields = ["id", "dt_created", "dt_updated"]


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            "Пример: создать договор поставки",
            value={
                "supplier": 1,
                "storage": 1,
                "employee_entered_contract": 1,
                "supplier_contact": 1,
                "is_active": True,
                "expiration_date": "2026-12-31",
            },
            request_only=True,
        )
    ]
)
class SupplyContractRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplyContract
        fields = "__all__"
        read_only_fields = ["id", "dt_created", "dt_updated"]


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            "Пример: добавить товар в договор",
            value={
                "supply_contract": 1,
                "product": 10,
                "price": 999,
                "quantity": 100,
                "delivery_frequency": "weekly",
            },
            request_only=True,
        )
    ]
)
class SupplyContractProductRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplyContractProduct
        fields = "__all__"
        read_only_fields = ["id", "dt_created", "dt_updated"]
    

@extend_schema_serializer(
    examples=[
        OpenApiExample(
            "Пример: создать поставку",
            value={
                "storage": 1,
                "supply_contract": 1,
                "created_by": 1,
                "received_by": None,
                "planned_date": "2026-01-10",
                "arrived_at": "2026-01-10T10:00:00Z",
                "status": "draft",
            },
            request_only=True,
        )
    ]
)
class SupplyRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supply
        fields = "__all__"
        read_only_fields = ["id", "dt_created", "dt_updated"]
        
        
@extend_schema_serializer(
    examples=[
        OpenApiExample(
            "Пример: добавить продукт в поставку",
            value={
                "supply": 1,
                "product": 10,
                "supply_contract_product": 5,
                "quantity_actual_total": 0,
                "quantity_expected": 100,
                "requires_review": True,
                "status": "has_issues",
                "purchase_price": 999,
            },
            request_only=True,
        )
    ]
)
class SupplyProductRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplyProduct
        fields = "__all__"
        read_only_fields = ["id", "dt_created", "dt_updated"]
        
        
@extend_schema_serializer(
    examples=[
        OpenApiExample(
            "Пример: добавить партию (факт)",
            value={
                "supply_product": 1,
                "manufacture_date": "2026-01-01",
                "expiry_date_actual": "2026-12-31",
                "quantity_actual": 50,
                "packaging_condition": "good",
                "status": "draft",
            },
            request_only=True,
        )
    ]
)
class SupplyProductLotRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplyProductLot
        fields = "__all__"
        read_only_fields = ["id", "dt_created", "dt_updated"]
        
        
@extend_schema_serializer(
    examples=[
        OpenApiExample(
            "Пример: причина несоответствия",
            value={"name": "Истёк срок годности"},
            request_only=True,
        )
    ]
)
class DiscrepancyReasonRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscrepancyReason
        fields = "__all__"
        read_only_fields = ["id", "dt_created", "dt_updated"]
        
        
@extend_schema_serializer(
    examples=[
        OpenApiExample(
            "Пример: создать несоответствие",
            value={
                "supply_product_lot": 1,
                "discrepancy_reason": 1,
                "created_by": 1,
                "decided_by": None,
                "comment": "Упаковка повреждена",
                "status": "open",
                "decided_at": None,
                "decision_comment": "",
            },
            request_only=True,
        )
    ]
)
class SupplyDiscrepancyRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplyDiscrepancy
        fields = "__all__"
        read_only_fields = ["id", "dt_created", "dt_updated"]
        
        
class DiscrepancyAttachmentRequestSerializer(serializers.ModelSerializer):
    """
    file — multipart/form-data
    supply_discrepancy — обычное поле (id заявки)
    """
    
    class Meta:
        model = DiscrepancyAttachment
        fields = "__all__"
        read_only_fields = ["id", "dt_created", "dt_updated"]