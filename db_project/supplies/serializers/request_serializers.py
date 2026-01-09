from drf_spectacular.utils import OpenApiExample, extend_schema_serializer
from rest_framework import serializers

from supplies.models import Supplier, SupplierContact, SupplyContract, SupplyContractProduct


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