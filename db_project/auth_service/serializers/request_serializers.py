from cfgv import ValidationError
from django.contrib.auth.password_validation import (
    validate_password as django_validate_password,
)
from drf_spectacular.utils import extend_schema_serializer, OpenApiExample
from rest_framework import serializers

from common_utils import constants
from employees.models import Employee, Passport


@extend_schema_serializer(
    many=False,
    examples=[
        OpenApiExample(
            'Стандартный ответ',
            value={
                'old_password': 'test',
                'new_password': 'test1',
                'new_password2': 'test1',
            },
        ),
    ],
)
class ChangePasswordRequestSerializer(serializers.Serializer):
    """Сериализатор ответа для смены пароля"""

    old_password = serializers.CharField(help_text='Старый пароль')
    new_password = serializers.CharField(help_text='Новый пароль')
    new_password2 = serializers.CharField(help_text='Новый пароль (еще раз)')

    def validate_old_password(self, old_password_value):
        """Проверить, что старый пароль введен верно"""
        if not self.context['user'].check_password(old_password_value):
            raise serializers.ValidationError('Старый пароль неверный')

        return old_password_value

    def validate_new_password(self, new_password_value):
        """Проверить новый пароль"""
        django_validate_password(new_password_value, user=self.context['user'])
        return new_password_value

    def validate(self, obj):
        """Проверка"""
        if obj['old_password'] == obj['new_password']:
            raise serializers.ValidationError('Новый пароль совпадает со старым')
        if obj['new_password'] != obj['new_password2']:
            raise serializers.ValidationError('Пароли не совпадают')

        return obj


@extend_schema_serializer(
    many=False,
    examples=[
        OpenApiExample(
            'Стандартный запрос',
            value={
                'username': 'username',
                'email': 'email',
                'last_name': 'last_name',
                'first_name': 'first_name',
                'second_name': 'second_name',
                'gender': 'male',
                'phone': 'phone',
                'birth_date': '2020-10-10',
                'snils': '11111111111',
                'inn': '111111111111',
                'work_phone': '79180000000',
            },
        ),
    ],
)
class EmployeeRequestSerializer(serializers.ModelSerializer):
    """Сериализатор модели Employee"""

    class Meta:
        model = Employee
        fields = [
            'username',
            'email',
            'last_name',
            'first_name',
            'second_name',
            'phone',
            'birth_date',
            'gender',
            'snils',
            'inn',
            'work_phone',
            'phone',
        ]


@extend_schema_serializer(
    many=False,
    examples=[
        OpenApiExample(
            'Стандартный запрос',
            value={
                'username': 'username',
                'email': 'email@email.com',
                'last_name': 'last_name',
                'first_name': 'first_name',
                'second_name': 'second_name',
                'gender': 'male',
                'phone': 'phone',
                'birth_date': '2020-10-10',
                'passport': '1',
                'snils': '11111111111',
                'inn': '111111111111',
                'work_phone': '79180000000',

                'type': 'simple',
                'series': '1233',
                'number': '123456',
                'issue_date': '2025-10-17',
                'issued_by': 'test',
                'authority_code': '230-123',
                'registration_address': 'test',
                'residential_address': 'test',

                'password': 'password',
                'password2': 'password2',
            },
        ),
    ],
)
class RegisterEmployeeRequestSerializer(serializers.Serializer):
    """Сериализатор запроса модели Employee"""

    username = serializers.CharField(help_text='Имя пользователя', max_length=150)
    email = serializers.EmailField(help_text='Электронная почта', allow_blank=True)
    last_name = serializers.CharField(
        help_text='Фамилия', allow_blank=True, max_length=60
    )
    first_name = serializers.CharField(help_text='Имя', allow_blank=True, max_length=60)
    second_name = serializers.CharField(
        help_text='Отчество', allow_blank=True, max_length=60
    )
    birth_date = serializers.DateField(help_text='Дата рождения')
    gender = serializers.ChoiceField(help_text='Пол', choices=constants.GENDER_CHOICES)
    phone = serializers.CharField(help_text='Номер телефона', allow_blank=True, max_length=13)
    work_phone = serializers.CharField(help_text='Рабочий телефон', allow_blank=True, max_length=13)
    snils = serializers.CharField(help_text='СНИЛС', max_length=11)
    inn = serializers.CharField(help_text='ИНН', max_length=12)

    # passport
    type = serializers.ChoiceField(help_text='Тип паспорта', choices=constants.PASSPORT_TYPES)
    series = serializers.CharField(help_text='Серия', max_length=4)
    number = serializers.CharField(help_text='Номер', max_length=7)
    issue_date = serializers.DateField(help_text='Дата выдачи')
    issued_by = serializers.CharField(help_text='Кем выдан', max_length=255)
    authority_code = serializers.CharField(help_text='Код подразделения', max_length=7)
    registration_address = serializers.CharField(help_text='Адрес регистрации', allow_blank=True)
    residential_address = serializers.CharField(help_text='Адрес фактического проживания', allow_blank=True)

    password = serializers.CharField(help_text='Пароль', max_length=128)
    password2 = serializers.CharField(help_text='Пароль (еще раз)', max_length=128)

    def validate_username(self, username):
        """Проверить имя пользователя"""
        if Employee.objects.filter(username=username).exists():
            raise ValidationError('Пользователь с таким именем уже существует')

        return username

    def validate_password(self, password):
        """Проверить пароль"""
        django_validate_password(password)
        return password

    def validate(self, obj):
        """Проверка"""
        if Passport.objects.filter(type=obj['type'], series=obj['series'], number=['number']).exists():
            raise serializers.ValidationError('Паспорт уже добавлен в базу')

        if obj['password'] != obj['password2']:
            raise serializers.ValidationError('Пароли не совпадают')

        return obj
