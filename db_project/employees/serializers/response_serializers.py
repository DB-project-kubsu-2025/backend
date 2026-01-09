from drf_spectacular.utils import OpenApiExample, extend_schema_serializer
from rest_framework import serializers
from django.contrib.auth.models import Group

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


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ["id", "name"]


@extend_schema_serializer(
    many=True,
    examples=[
        OpenApiExample(
            'Пример ответа от сервера',
            description="Базовый ответ паспорта",
            value=[
                {
                    "id": 1,
                    "type": "SIMPLE",
                    "series": "1234",
                    "number": "567891",
                    "issue_date": "2020-01-01",
                    "issued_by": "ОВД г.Пример",
                    "authority_code": "770-001",
                }
            ],
        )
    ],
)
class PassportResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passport
        fields = [
            "id",
            "type",
            "series",
            "number",
            "issue_date",
            "issued_by",
            "authority_code",
            "registration_address",
            "residential_address",
            "dt_created",
            "dt_updated",
        ]


@extend_schema_serializer(
    many=True,
    examples=[
        OpenApiExample(
            'Пример ответа от сервера',
            description="Базовый ответ",
            value=[{"id": 1, "name": "1.0", "monthly_output": 160}],
        )
    ],
)
class WorkingRateResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkingRate
        fields = ["id", "name", "monthly_output"]


@extend_schema_serializer(
    many=True,
    examples=[
        OpenApiExample(
            'Пример ответа от сервера',

            description="Базовый ответ",
            value=[{"id": 155, "name": "Кассир"}],
        )
    ],
)
class JobPositionResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPosition
        fields = ["id", "name"]


class SalaryResponseSerializer(serializers.ModelSerializer):
    job_position = JobPositionResponseSerializer(read_only=True)
    working_rate = WorkingRateResponseSerializer(read_only=True)

    class Meta:
        model = Salary
        fields = ["id", "amount", "job_position", "working_rate", "dt_created", "dt_updated"]


class WorkplaceResponseSerializer(serializers.ModelSerializer):
    storage = serializers.PrimaryKeyRelatedField(read_only=True)
    main_office_filial = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Workplace
        fields = ["id", "storage", "main_office_filial", "dt_created", "dt_updated"]


@extend_schema_serializer(
    many=True,
    examples=[
        OpenApiExample(
            'Пример ответа от сервера',

            description="Базовый ответ",
            value=[
                {
                    "id": 1,
                    "username": "ivanov",
                    "first_name": "Иван",
                    "last_name": "Иванов",
                    "second_name": "Иванович",
                    "email": "ivanov@example.com",
                    "birth_date": "1990-01-01",
                    "gender": "male",
                    "snils": "12345678901",
                    "inn": "123456789012",
                    "phone": "79001234567",
                    "work_phone": "74951234567",
                    "passport": 1,
                    "workplace": 1,
                    "groups": [{"id": 1, "name": "staff"}],
                }
            ],
        )
    ],
)
class EmployeeResponseSerializer(serializers.ModelSerializer):
    passport = PassportResponseSerializer(read_only=True)
    workplace = WorkplaceResponseSerializer(read_only=True)
    salaries = SalaryResponseSerializer(many=True, read_only=True)
    groups = GroupSerializer(many=True, read_only=True)

    class Meta:
        model = Employee
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "second_name",
            "email",
            "birth_date",
            "gender",
            "snils",
            "inn",
            "phone",
            "work_phone",
            "passport",
            "workplace",
            "salaries",
            "groups",
            "is_active",
            "is_staff",
            "date_joined",
            "dt_created",
            "dt_updated",
        ]


@extend_schema_serializer(
    many=True,
    examples=[
        OpenApiExample(
            'Пример ответа от сервера',
            description="Базовый ответ",
            value=[{"id": 1, "name": "Больничный", "counts_against_annual": True}],
        )
    ],
)
class LeaveRequestTypeResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveRequestType
        fields = ["id", "name", "counts_against_annual", "requires_documents", "documents_due_days"]


class LeaveRequestAttachmentResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveRequestAttachment
        fields = ["id", "leave_request", "file", "dt_created"]


class LeaveRequestResponseSerializer(serializers.ModelSerializer):
    employee = EmployeeResponseSerializer(read_only=True)
    approved_by = EmployeeResponseSerializer(read_only=True)
    attachments = LeaveRequestAttachmentResponseSerializer(many=True, read_only=True)

    class Meta:
        model = LeaveRequest
        fields = [
            "id",
            "employee",
            "approved_by",
            "status",
            "start_date",
            "end_date",
            "approved_at",
            "comment",
            "documents_received_at",
            "attachments",
            "dt_created",
            "dt_updated",
        ]


class AnnualLeaveBalanceResponseSerializer(serializers.ModelSerializer):
    employee = EmployeeResponseSerializer(read_only=True)

    class Meta:
        model = AnnualLeaveBalance
        fields = ["id", "employee", "year", "base_days", "carry_in_days", "manual_adjust_days", "dt_created"]


class TimeEntryResponseSerializer(serializers.ModelSerializer):
    employee = EmployeeResponseSerializer(read_only=True)

    class Meta:
        model = TimeEntry
        fields = ["id", "employee", "date", "minutes", "comment", "dt_created"]


class TimeSessionCloseReasonResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSessionCloseReason
        fields = ["id", "name"]


class TimeSessionResponseSerializer(serializers.ModelSerializer):
    employee = EmployeeResponseSerializer(read_only=True)
    close_reason = TimeSessionCloseReasonResponseSerializer(read_only=True)

    class Meta:
        model = TimeSession
        fields = ["id", "employee", "close_reason", "closed", "login_at", "logout_at", "dt_created"]


class TimeDayResponseSerializer(serializers.ModelSerializer):
    employee = EmployeeResponseSerializer(read_only=True)
    adjustment_reason = TimeSessionCloseReasonResponseSerializer(read_only=True)

    class Meta:
        model = TimeDay
        fields = ["id", "employee", "date", "comment", "adjusted_minutes", "adjustment_reason", "dt_created"]