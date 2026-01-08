from django.db import models

from common_utils.mixins import AutoDateMixin


class Region(AutoDateMixin):
    """Регион"""

    name = models.CharField(verbose_name='Название', max_length=64)

    class Meta:
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'

    def __str__(self):
        return self.name


class City(AutoDateMixin):
    """Город"""

    region = models.ForeignKey(
        'Region',
        verbose_name='Регион',
        on_delete=models.PROTECT,
        related_name='cities',
    )
    name = models.CharField(verbose_name='Название', max_length=64)

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return self.name


class MainOfficeFilial(AutoDateMixin):
    """Филиал головного офиса"""

    city = models.ForeignKey(
        'City',
        verbose_name='Город',
        on_delete=models.PROTECT,
        related_name='main_office_filials',
    )
    director = models.OneToOneField(
        'employees.Employee',
        verbose_name='Директор',
        on_delete=models.PROTECT,
        related_name='main_office_filial',
    )
    cadastral_number = models.CharField(verbose_name='Кадастровый номер', max_length=20)
    address = models.CharField(verbose_name='Адрес', max_length=128)

    class Meta:
        verbose_name = 'Филиал головного офиса'
        verbose_name_plural = 'Филиалы головного офиса'

    def __str__(self):
        return f'Филиал ГК по адресу: {self.city.name} {self.address}'


class StorageOpeningRequest(AutoDateMixin):
    """Запрос на открытие ТТ/хранилища"""

    storage = models.ForeignKey(
        'shops.Storage',
        verbose_name='Хранилище',
        on_delete=models.PROTECT,
    )
    main_office_filial = models.ForeignKey(
        'offices.MainOfficeFilial',
        verbose_name='Филиал ГК',
        on_delete=models.PROTECT,
    )
    confirmed_by = models.ForeignKey(
        'employees.Employee',
        verbose_name='Кем подтверждено',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    is_confirmed = models.BooleanField(verbose_name='Подтверждено', default=False)
    confirmation_date = models.DateField(verbose_name='Дата подтверждения', null=True, blank=True)

    class Meta:
        verbose_name = 'Запрос на открытие ТТ/хранилища'
        verbose_name_plural = 'Запросы на открытие ТТ/хранилища'

    def __str__(self):
        return f'Запрос №{self.id} {self.storage} {self.main_office_filial}'
