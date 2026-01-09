from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from rest_framework import serializers

from employees.models import Passport, Workplace
from shops.models import Storage
from offices.models import MainOfficeFilial

User = get_user_model()


class GroupBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("id", "name")


class PassportSerializer(serializers.ModelSerializer):
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


class StorageBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storage
        fields = ["id", "cadastral_number", "approved_by_main_company", "opened"]


class MainOfficeFilialBriefSerializer(serializers.ModelSerializer):
    city_name = serializers.SerializerMethodField()

    class Meta:
        model = MainOfficeFilial
        fields = ["id", "cadastral_number", "address", "city_name"]

    def get_city_name(self, obj):
        return getattr(obj.city, "name", None)


class WorkplaceSerializer(serializers.ModelSerializer):
    storage = StorageBriefSerializer(read_only=True)
    main_office_filial = MainOfficeFilialBriefSerializer(read_only=True)

    class Meta:
        model = Workplace
        fields = ["id", "storage", "main_office_filial", 'working_rate', "dt_created", "dt_updated"]


class UserFullSerializer(serializers.ModelSerializer):
    passport = PassportSerializer(read_only=True)
    workplace = WorkplaceSerializer(read_only=True)
    groups = GroupBriefSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "second_name",
            "birth_date",
            "gender",
            "snils",
            "inn",
            "phone",
            "work_phone",
            # meta
            "is_active",
            "is_staff",
            "is_superuser",
            "date_joined",
            # relations
            "passport",
            "workplace",
            "groups",
            "dt_created",
            "dt_updated",
        ]
        read_only_fields = fields