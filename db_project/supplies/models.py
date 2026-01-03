from django.db import models

from common_utils.mixins import AutoDateMixin


class Supplier(AutoDateMixin):
    """Поставщик"""

    name = models.CharField(verbose_name='Название', max_length=255)
    address = models.CharField(verbose_name='Адрес', max_length=255)
    ogrn = models.CharField(verbose_name='ОГРН', max_length=13)
    inn = models.CharField(verbose_name='ИНН', max_length=12)
    kpp = models.CharField(verbose_name='КПП', max_length=9)
    bank_name = models.CharField(verbose_name='Наименование банка', max_length=255)
    bik = models.CharField(verbose_name='БИК', max_length=9)
    corr_account = models.CharField(verbose_name='Корреспондентский счет', max_length=20)
    checking_account = models.CharField(verbose_name='Расчетный счет', max_length=20)
    swift = models.CharField(verbose_name='Swift', max_length=11)
    iban = models.CharField(verbose_name='IBan', max_length=34)

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'
        ordering = ['name']

    def __str__(self):
        return f'{self.name} {self.inn}'


class SupplierContact(AutoDateMixin):
    """Контактное лицо поставщика"""

    supplier = models.ForeignKey(
        'Supplier',
        verbose_name='Поставщик',
        on_delete=models.PROTECT,
    )
    passport = models.ForeignKey(
        'employees.Passport',
        verbose_name='Паспорт',
        on_delete=models.PROTECT,
    )
    surname = models.CharField(verbose_name='Фамилия', max_length=40)
    first_name = models.CharField(verbose_name='Имя', max_length=40)
    second_name = models.CharField(verbose_name='Отчество', max_length=40, blank=True, default='')
    snils = models.CharField(verbose_name='СНИЛС', max_length=14)
    inn = models.CharField(verbose_name='ИНН', max_length=12)
    phone = models.CharField(verbose_name='Номер телефона', max_length=15)
    email = models.EmailField(verbose_name='Электронная почта', max_length=255)
    job_title = models.CharField(verbose_name='Должность', max_length=80)

    class Meta:
        verbose_name = 'Контактное лицо поставщика'
        verbose_name_plural = 'Контактные лица поставщиков'

    def __str__(self):
        return f'{self.surname} {self.first_name}, {self.supplier.name}, {self.phone}'


# class SupplyContract(AutoDateMixin):
#     """Договор на поставку"""
# todo:


# class SupplyContractProduct(AutoDateMixin):
#     """Связь продукт - контракт на поставку"""
#     # todo:


# class Supply(AutoDateMixin):
#     """Поставка"""
#     # todo:


# class SupplyProduct(AutoDateMixin):
#     """Связка продукт - поставка"""
#     # todo:


# class SupplyProductLot(AutoDateMixin):
#     """Связка продукт в поставке - партия"""
#     # todo:


class DiscrepancyReason(AutoDateMixin):
    """Причина несоответствия поставки ожиданиям"""

    name = models.CharField(verbose_name='Название', max_length=255)

    class Meta:
        verbose_name = 'Причина несоответствия поставки ожиданиям'
        verbose_name_plural = 'Причины несоответствия поставки ожиданиям'

    def __str__(self):
        return self.name


# class SupplyDiscrepancy(AutoDateMixin):
#     """Несоответствие поставки ожиданиям"""
#     # todo:


# class DiscrepancyAttachment(AutoDateMixin):
#     """Вложение для несоответствий"""
#     # todo:
