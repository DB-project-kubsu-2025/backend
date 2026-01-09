from drf_spectacular.utils import OpenApiExample, extend_schema_serializer
from rest_framework import serializers

from employees.models import (
    Passport,
    WorkingRate,
    JobPosition,
    Salary,
    Workplace,
    Employee,
    LeaveRequestType,
    LeaveRequest,
    LeaveRequestAttachment,
    AnnualLeaveBalance,
    TimeEntry,
    TimeSessionCloseReason,
    TimeSession,
    TimeDay,
)


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            "Пример запроса на создание паспорта",
            description="Базовый запрос",
            value={
                "type": "Обычный",
                "series": "1234",
                "number": "567801",
                "issue_date": "2020-01-01",
                "issued_by": "ОВД г.Пример",
                "authority_code": "770-001",
                "registration_address": "г. Пример, ул. Главная, 1",
                "residential_address": "г. Пример, ул. Главная, 1",
            },
            request_only=True,
        )
    ]
)
class PassportRequestSerializer(serializers.ModelSerializer):
    """Сериализатор запроса для создания/обновления Passport"""

    class Meta:
        model = Passport
        fields = [
            "type",
            "series",
            "number",
            "issue_date",
            "issued_by",
            "authority_code",
            "registration_address",
            "residential_address",
        ]


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            "Пример запроса на создание рабочей ставки",
            description="Базовый запрос",
            value={"name": "0.75", "monthly_output": 120},
            request_only=True,
        )
    ]
)
class WorkingRateRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkingRate
        fields = ["name", "monthly_output"]


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            "Пример запроса на создание должности",
            description="Базовый запрос",
            value={"name": "Менеджер"},
            request_only=True,
        )
    ]
)
class JobPositionRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPosition
        fields = ["name"]


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            "Пример запроса на создание зарплаты",
            description="Базовый запрос",
            value={"amount": 35000, "job_position": 1, "working_rate": 1},
            request_only=True,
        )
    ]
)
class SalaryRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salary
        fields = ["amount", "job_position", "working_rate"]


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            "Пример запроса на создание рабочего места",
            description="Базовый запрос",
            value={"storage": 1, "main_office_filial": None},
            request_only=True,
        )
    ]
)
class WorkplaceRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workplace
        fields = ["storage", "main_office_filial"]


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            "Пример запроса на создание сотрудника",
            description="Базовый запрос",
            value={
                "username": "employee_1",
                "password": "123456789abc",
                "first_name": "Иван",
                "last_name": "Иванов",
                "second_name": "Иванович",
                "email": "ivanov@example.com",
                "birth_date": "1990-01-01",
                "gender": "male",
                "passport": 1,
                "snils": "12345678901",
                "inn": "123456789012",
                "phone": "79001234567",
                "work_phone": "74951234567",
                "workplace": 1,
            },
            request_only=True,
        )
    ]
)
class EmployeeRequestSerializer(serializers.ModelSerializer):
    """Сериализатор запроса для создания/обновления Employee"""
    password = serializers.CharField(write_only=True, required=False, allow_blank=False)

    class Meta:
        model = Employee
        fields = [
            "username",
            "password",
            "first_name",
            "last_name",
            "second_name",
            "email",
            "birth_date",
            "gender",
            "passport",
            "snils",
            "inn",
            "phone",
            "work_phone",
            "workplace",
        ]


    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        for attr, val in validated_data.items():
            setattr(instance, attr, val)
        if password:
            instance.set_password(password)
        instance.save()
        return instance

class EmployeeAdminRequestSerializer(EmployeeRequestSerializer):
    class Meta(EmployeeRequestSerializer.Meta):
        fields = EmployeeRequestSerializer.Meta.fields + ["is_active", "is_staff"]


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            "Пример запроса на создание типа запроса на временное отсутствие",
            description="Базовый запрос",
            value={"name": "Больничный", "counts_against_annual": False, "requires_documents": True, 'documents_due_days': 3},
            request_only=True,
        )
    ]
)
class LeaveRequestTypeRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveRequestType
        fields = ["name", "counts_against_annual", "requires_documents", "documents_due_days"]


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            "Пример запроса на создание запроса на отсутствие",
            description="Базовый запрос",
            value={
                "employee": 1,
                "status": "ON_APPROVAL",
                "start_date": "2025-01-01",
                "end_date": "2025-01-03",
                'type': 2,
                "comment": "По семейным обстоятельствам",
            },
            request_only=True,
        )
    ]
)
class LeaveRequestRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveRequest
        fields = ["employee", "approved_by", "status",'type', "start_date", "end_date", "comment", "documents_received_at"]


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            "Пример запроса на добавление вложения к запросу на отсутствие",
            description="Базовый запрос",
            value={"leave_request": 17, "file": "binary multipart/form-data"},
            request_only=True,
        )
    ]
)
class LeaveRequestAttachmentRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveRequestAttachment
        fields = ["leave_request", "file"]


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            "Пример запроса на корректировку отпуска (баланс)",
            description="Базовый запрос",
            value={"employee": 1, "year": 2025, "base_days": 28, "carry_in_days": 3, "manual_adjust_days": 0},
            request_only=True,
        )
    ]
)
class AnnualLeaveBalanceRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnnualLeaveBalance
        fields = ["employee", "year", "base_days", "carry_in_days", "manual_adjust_days"]


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            "Пример запроса на списание времени",
            description="Базовый запрос",
            value={"employee": 1, "date": "2025-01-01", "minutes": 60, "comment": "Корректировка"},
            request_only=True,
        )
    ]
)
class TimeEntryRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeEntry
        fields = ["employee", "date", "minutes", "comment"]


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            "Пример запроса на причину закрытия сессии",
            description="Базовый запрос",
            value={"name": "Перерыв"},
            request_only=True,
        )
    ]
)
class TimeSessionCloseReasonRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSessionCloseReason
        fields = ["name"]


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            "Пример запроса на создание рабочей сессии",
            description="Базовый запрос",
            value={"employee": 1, "login_at": "2025-01-01T08:00:00Z", "logout_at": None},
            request_only=True,
        )
    ]
)
class TimeSessionRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSession
        fields = ["employee", "close_reason", "closed", "login_at", "logout_at"]


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            "Пример запроса на создание сводки по дню",
            description="Базовый запрос",
            value={"employee": 1, "date": "2025-01-01", "adjusted_minutes": 0, "comment": ""},
            request_only=True,
        )
    ]
)
class TimeDayRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeDay
        fields = ["employee", "date", "comment", "adjusted_minutes", "adjustment_reason"]