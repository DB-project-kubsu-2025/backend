from django.contrib.auth.models import AbstractUser
from django.db import models

from common_utils import constants
from common_utils.mixins import AutoDateMixin


class Passport(AutoDateMixin):
    """Модель: паспорт"""

    type = models.CharField(verbose_name='Тип паспорта', choices=constants.PASSPORT_TYPES)
    series = models.CharField(verbose_name='Серия', max_length=4)
    number = models.CharField(verbose_name='Номер', max_length=7)
    issue_date = models.DateField(verbose_name='Дата выдачи')
    issued_by = models.CharField(verbose_name='Кем выдан', max_length=255)
    authority_code = models.CharField(verbose_name='Код подразделения', max_length=7)
    registration_address = models.CharField(verbose_name='Адрес регистрации', blank=True, default='')
    residential_address = models.CharField(verbose_name='Адрес фактического проживания', blank=True, default='')

    class Meta:
        verbose_name = 'Паспорт'
        verbose_name_plural = 'Паспорта'
        unique_together = ['type', 'series', 'number']

    def __str__(self):
        """Строковое представление"""
        return f'{self.series} {self.number}'


class Employee(AbstractUser, AutoDateMixin):
    """Модель: Работник"""

    second_name = models.CharField(verbose_name='Отчество', max_length=50, blank=True, default='')
    birth_date = models.DateField(verbose_name='Дата рождения')

    gender = models.CharField(verbose_name='Пол', choices=constants.GENDER_CHOICES)
    passport = models.OneToOneField(
        'Passport',
        verbose_name='Паспорт',
        on_delete=models.PROTECT,
        related_name='employee',
    )
    snils = models.CharField(verbose_name='СНИЛС', max_length=11, unique=True)
    inn = models.CharField(verbose_name='ИНН', max_length=12, unique=True)
    work_phone = models.CharField(verbose_name='Рабочий телефон', max_length=11)
    phone = models.CharField(verbose_name='Рабочий телефон', max_length=11, blank=True, default='')


    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'

    def __str__(self):
        """Строковое представление"""
        return f'{self.work_phone} - {self.last_name} {self.first_name}'

    @property
    def is_foreign_worker(self):
        """Является ли работник иностранцем"""
        return self.passport.type == constants.FOREIGN
