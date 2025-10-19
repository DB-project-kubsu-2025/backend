import datetime

from django.core.management import BaseCommand

from auth_service.models import Passport, Employee
from common_utils import constants


class Command(BaseCommand):
    """
    Создать кастомного суперпользователя
    Дефолтная джанговская команда поломана, так как была переопределена модель User, в которой указан not-null
    FK на модель паспорта
    """

    def handle(self, *args, **options):
        """Метод выполнения команды"""
        admin_passport = Passport.objects.create(
            type=constants.SIMPLE,
            series='0000',
            number='000000',
            issue_date=datetime.date(2020, 10, 10),
            issued_by='',
            authority_code='',
            registration_address='',
            residential_address='',
        )

        employee = Employee(
            is_staff=True,
            is_superuser=True,
            username='admin',
            email='admin.admin@test.com',
            first_name='Админ',
            last_name='Админов',
            second_name='Админович',
            birth_date=datetime.date(2000, 10, 10),
            gender=constants.MALE,
            passport=admin_passport,
            snils='12345678901',
            inn='123456789012',
            work_phone='79998887766',
            phone='79998887766',
        )
        employee.set_password('1234')
        employee.save()
