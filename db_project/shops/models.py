from django.db import models

from common_utils.mixins import AutoDateMixin
from shops.utils import generate_file_path


class ProductUnit(AutoDateMixin):
    """Единица измерения"""

    name = models.CharField(verbose_name='Название', max_length=32)

    class Meta:
        verbose_name = 'Единица измерения'
        verbose_name_plural = 'Справочник единиц измерения'

    def __str__(self):
        return self.name


class ProductCategory(AutoDateMixin):
    """Единица измерения"""

    name = models.CharField(verbose_name='Название', max_length=64)

    class Meta:
        verbose_name = 'Категория продукта'
        verbose_name_plural = 'Справочник категорий продуктов'

    def __str__(self):
        return self.name


class Product(AutoDateMixin):
    """Справочник продуктов"""

    unit = models.ForeignKey(
        'ProductUnit',
        verbose_name='Единица измерения',
        on_delete=models.PROTECT,
    )
    category = models.ForeignKey(
        'ProductCategory',
        verbose_name='Категория продукта',
        on_delete=models.PROTECT,
    )
    name = models.CharField(verbose_name='Название', max_length=128)
    description = models.CharField(verbose_name='Описание', max_length=300, blank=True, default='')
    expiration_days = models.PositiveSmallIntegerField(verbose_name='Кол-во дней до истечения срока годности')
    producer_name = models.CharField(verbose_name='Производитель', max_length=128)
    producer_code = models.UUIDField(verbose_name='Код производителя')
    country_name = models.CharField(verbose_name='Страна', max_length=64)
    additional_info = models.CharField(verbose_name='Дополнительная информация', max_length=300)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Справочник продуктов'
        ordering = ['name']

    def __str__(self):
        return self.name


class StorageProfile(AutoDateMixin):
    """Требуемое условие хранения продукта"""

    product = models.ForeignKey(
        'Product',
        verbose_name='Продукт',
        on_delete=models.PROTECT,
        related_name='storage_profiles',
    )
    weight = models.PositiveSmallIntegerField(verbose_name='Вес (в кг)')
    temp_min_c = models.SmallIntegerField(verbose_name='Мин. температура (Цельсия)')
    temp_max_c = models.SmallIntegerField(verbose_name='Макс. температура (Цельсия)')
    light_sensitive = models.BooleanField(verbose_name='Чувствителен к свету', default=False)

    class Meta:
        verbose_name = 'Требуемое условие хранения продукта'
        verbose_name_plural = 'Требуемые условия хранения продуктов'
        ordering = ['dt_created']

    def __str__(self):
        return f'Условие для {self.product.name} id={self.id}'


class ProductMedia(AutoDateMixin):
    """Медиа для карточки товара"""

    product = models.ForeignKey(
        'Product',
        verbose_name='Продукт',
        on_delete=models.PROTECT,
    )
    image = models.ImageField(
        upload_to=generate_file_path,
        verbose_name='Медиа',
    )

    class Meta:
        verbose_name = 'Медиа для карточки товара'
        verbose_name_plural = 'Медиа для карточек товаров'

    def __str__(self):
        return f'Медиа для {self.product.name} id={self.id}'


class StorageType(AutoDateMixin):
    """Тип хранилища"""

    name = models.CharField(verbose_name='Название', max_length=32)

    class Meta:
        verbose_name = 'Тип хранилища'
        verbose_name_plural = 'Типы хранилища'

    def __str__(self):
        return self.name


class Storage(AutoDateMixin):
    """Хранилище"""

    director = models.OneToOneField(
        'employees.Employee',
        verbose_name='Директор',
        on_delete=models.PROTECT,
    )
    main_office_filial = models.ForeignKey(
        'offices.MainOfficeFilial',
        verbose_name='Филиал ГК',
        on_delete=models.PROTECT,
        related_name='storages',
    )
    storage_type = models.ForeignKey(
        'StorageType',
        verbose_name='Тип хранилища',
        on_delete=models.PROTECT,
    )
    cadastral_number = models.CharField(verbose_name='Кадастровый номер', max_length=20, unique=True)
    approved_by_main_company = models.BooleanField(verbose_name='Подтверждено ГК', default=False)
    opened = models.BooleanField(verbose_name='Действующий', default=False)
    area = models.PositiveSmallIntegerField(verbose_name='Площадь (в кв. м.)')
    utilization_percent = models.PositiveSmallIntegerField(verbose_name='Процент утилизации', null=True, blank=True)

    class Meta:
        verbose_name = 'Хранилище'
        verbose_name_plural = 'Хранилища'
        ordering = ['dt_created']

    def __str__(self):
        return self.cadastral_number
