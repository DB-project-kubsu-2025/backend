from pickle import GLOBAL

from django.db import models
from django.utils import timezone

from common_utils.mixins import AutoDateMixin
from shops.utils import generate_file_path


class ProductUnit(AutoDateMixin):
    """Единица измерения"""

    name = models.CharField(verbose_name='Название', max_length=32, unique=True)

    class Meta:
        verbose_name = 'Единица измерения'
        verbose_name_plural = 'Справочник единиц измерения'

    def __str__(self):
        return self.name


class ProductCategory(AutoDateMixin):
    """Единица измерения"""

    name = models.CharField(verbose_name='Название', max_length=64, unique=True)

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


class ProductInventoryLot(AutoDateMixin):
    """Партия товара"""

    product = models.ForeignKey(
        'Product',
        verbose_name='Продукт',
        on_delete=models.PROTECT,
        related_name='inventory_lots',
    )
    supply_product = models.ForeignKey(
        'supplies.SupplyProduct',
        verbose_name='Продукт в поставке',
        on_delete=models.PROTECT,
    )
    manufacture_date = models.DateField(verbose_name='Дата изготовления')
    expiry_date = models.DateField(verbose_name='Дата истечения срока годности')
    barcode = models.UUIDField(verbose_name='Штрих-код')

    class Meta:
        verbose_name = 'Партия товара'
        verbose_name_plural = 'Партии товаров'

    def __str__(self):
        return f'Партия №{self.id}, {self.product}'


class StorageType(AutoDateMixin):
    """Тип хранилища"""

    name = models.CharField(verbose_name='Название', max_length=32, unique=True)

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


class SpaceType(AutoDateMixin):
    """Тип места хранения"""

    name = models.CharField(verbose_name='Название', max_length=64, unique=True)

    class Meta:
        verbose_name = 'Тип места хранения'
        verbose_name_plural = 'Типы мест хранения'
        ordering = ['name']

    def __str__(self):
        return self.name


class Space(AutoDateMixin):
    """Место хранения в хранилище"""

    storage = models.ForeignKey(
        'Storage',
        verbose_name='Хранилище',
        on_delete=models.PROTECT,
        related_name='store_spaces',
    )
    space_type = models.ForeignKey(
        'SpaceType',
        verbose_name='Тип хранилища',
        on_delete=models.PROTECT,
    )
    parent_space = models.ForeignKey(
        'self',
        verbose_name='Родительское место хранения',
        help_text='Для иерархии, например, при SALES_AREA',
        on_delete=models.PROTECT,
    )
    temp_min_c = models.SmallIntegerField(verbose_name='Мин. температура (Цельсия)')
    temp_max_c = models.SmallIntegerField(verbose_name='Макс. температура (Цельсия)')
    max_load = models.PositiveSmallIntegerField(verbose_name='Макс. загрузка (кг)')

    class Meta:
        verbose_name = 'Место хранения в хранилище'
        verbose_name_plural = 'Места хранения в хранилищах'

    def __str__(self):
        return f'Место хранения {self.space_type} в хранилище {self.storage}'


class InventoryLot(AutoDateMixin):
    """Партия товара"""

    product = models.ForeignKey(
        'Product',
        verbose_name='Продукт',
        on_delete=models.PROTECT,
    )
    supply_product_lot = models.ForeignKey(
        'supplies.SupplyProductLot',
        verbose_name='Фактическая партия в продуктах поставки',
        on_delete=models.PROTECT,
    )
    manufacture_date = models.DateField(verbose_name='Дата изготовления')
    expiry_date = models.DateField(verbose_name='Дата истечения срока годности')

    spaces = models.ManyToManyField(
        'Space',
        verbose_name='Места хранения',
        through='InventoryBalance',
        related_name='inventory_lots',
        blank=True,
    )

    class Meta:
        verbose_name = 'Партия товара'
        verbose_name_plural = 'Партии товаров'

    def __str__(self):
        return f'Партия №{self.id} продукта {self.product}'

class InventoryBalance(AutoDateMixin):
    """Связка партия - место хранения"""

    inventory_lot = models.ForeignKey(
        'InventoryLot',
        verbose_name='Партия товара',
        on_delete=models.PROTECT,
    )
    storage = models.ForeignKey(
        'Storage',
        verbose_name='Хранилище',
        on_delete=models.PROTECT,
    )
    space = models.ForeignKey(
        'Space',
        verbose_name='Место хранения',
        on_delete=models.PROTECT,
    )
    quantity = models.PositiveSmallIntegerField(verbose_name='Кол-во')

    class Meta:
        verbose_name = 'Связка партия - место хранения'
        verbose_name_plural = 'Связки партия - место хранения'

    def __str__(self):
        return f'Связка №{self.id} {self.inventory_lot} - {self.space} в хранилище {self.storage}'


class MovementType(AutoDateMixin):
    """Тип перемещения партии"""

    name = models.CharField(verbose_name='Название', max_length=64, unique=True)

    class Meta:
        verbose_name = 'Тип перемещения партии'
        verbose_name_plural = 'Типы перемещения партии'
        ordering = ['name']

    def __str__(self):
        return self.name


class InventoryMovement(AutoDateMixin):
    """Перемещение партии по хранилищу"""

    inventory_lot = models.ForeignKey(
        'InventoryLot',
        verbose_name='Партия товара',
        on_delete=models.PROTECT,
    )
    storage = models.ForeignKey(
        'Storage',
        verbose_name='Хранилище',
        on_delete=models.PROTECT,
    )
    space_from = models.ForeignKey(
        'Space',
        verbose_name='Место хранения, из которого совершено перемещение',
        help_text='Пустое, если поставка',
        on_delete=models.PROTECT,
        related_name='movements_from',
        null=True,
        blank=True,
    )
    space_to = models.ForeignKey(
        'Space',
        verbose_name='Место хранения, в которое совершено перемещение',
        help_text='Пустое, если продажа или кража',
        on_delete=models.PROTECT,
        related_name='movements_to',
        null=True,
        blank=True,
    )
    created_by = models.ForeignKey(
        'employees.Employee',
        verbose_name='Кем создано',
        on_delete=models.PROTECT,
    )
    movement_type = models.ForeignKey(
        'MovementType',
        verbose_name='Тип перемещения',
        on_delete=models.PROTECT,
    )
    supply = models.ForeignKey(
        'supplies.Supply',
        verbose_name='Поставка',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    # sales_receipt = models.ForeignKey( # todo:
    #     'SalesReceipt',
    #     verbose_name='',
    #     on_delete=models.PROTECT,
    #     null=True,
    #     blank=True,
    # )
    # writeoff_act = models.ForeignKey(
    #     'WrileoffAct',
    #     verbose_name='Акт списания',
    #     on_delete=models.PROTECT,
    #     null=True,
    #     blank=True,
    # )
    quantity = models.PositiveSmallIntegerField(verbose_name='Кол-во')

    class Meta:
        verbose_name = 'Перемещение партии по хранилищу'
        verbose_name_plural = 'Перемещения партий по хранилищам'

    def __str__(self):
        return f'Перемещение №{self.id} по хранилищу {self.storage}'


class PriceList(AutoDateMixin):
    """Прайс-лист"""

    RECEIVED = 'received'
    VALIDATED = 'validated'
    APPLIED = 'applied'
    REJECTED = 'rejected'
    STATUSES = {
        RECEIVED: 'Принят',
        VALIDATED: 'Проверен',
        APPLIED: 'Применен',
        REJECTED: 'Отклонен',
    }

    storage = models.ForeignKey(
        'Storage',
        verbose_name='Хранилище',
        on_delete=models.PROTECT,
    )
    received_at = models.DateTimeField(verbose_name='Время приёмки')
    business_date = models.DateField(verbose_name='День, когда прайс-лист действует')
    status = models.CharField(
        verbose_name='Статус',
        max_length=20,
        choices=STATUSES,
        default=RECEIVED,
    )

    class Meta:
        verbose_name = 'Прайс-лист'
        verbose_name_plural = 'Прайс-лист'
        ordering = ['-business_date']

    def __str__(self):
        return f'Прайс-лист №{self.id} в хранилище {self.storage}'


class PriceListType(AutoDateMixin):
    """Тип прайс-листа"""

    name = models.CharField(verbose_name='Название', max_length=64, unique=True)

    class Meta:
        verbose_name = 'Тип прайс-листа'
        verbose_name_plural = 'Типы прайс-листов'
        ordering = ['name']

    def __str__(self):
        return self.name


class PriceListBase(AutoDateMixin):
    """Основание формирования прайс-листа"""

    name = models.CharField(verbose_name='Название', max_length=64, unique=True)
    is_active = models.BooleanField(verbose_name='Активно', default=False)

    class Meta:
        verbose_name = 'Тип прайс-листа'
        verbose_name_plural = 'Типы прайс-листов'
        ordering = ['name']

    def __str__(self):
        return self.name


class PriceListProduct(AutoDateMixin):
    """Прайс-лист для продукта в хранилище"""

    price_list = models.ForeignKey(
        'PriceList',
        verbose_name='Прайс-лист',
        on_delete=models.PROTECT,
        related_name='products_in_price_list',
    )
    price_list_type = models.ForeignKey(
        'PriceListType',
        verbose_name='Тип прайс-листа',
        on_delete=models.PROTECT,
    )
    product = models.ForeignKey(
        'Product',
        verbose_name='Продукт',
        on_delete=models.PROTECT,
    )
    price_list_base = models.ForeignKey(
        'PriceListBase',
        verbose_name='Основание формирования прайс-листа',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    input_cost_vh = models.PositiveSmallIntegerField(verbose_name='Входная цена (ВХ)')
    final_price = models.PositiveSmallIntegerField(verbose_name='Итоговая цена')
    regular_price = models.PositiveSmallIntegerField(verbose_name='Регулярная цена')

    class Meta:
        verbose_name = 'Прайс-лист для продукта в хранилище'
        verbose_name_plural = 'Прайс-листы для продуктов в хранилищах'

    def __str__(self):
        return f'Прайс-лист №{self.id} для продукта {self.product} в прайс-листе №{self.price_list_id}'


class PricingConstraint(AutoDateMixin):
    """Ограничение на изменение цены"""

    GLOBAL = 'global'
    STORAGE = 'storage'
    CATEGORY = 'category'
    PRODUCT = 'product'
    SCOPES = {
        GLOBAL: 'Глобально',
        STORAGE: 'В рамках хранилища',
        CATEGORY: 'В рамках категории продукта',
        PRODUCT: 'В рамках продукта',
    }

    storage = models.ForeignKey(
        'Storage',
        verbose_name='Хранилище',
        on_delete=models.PROTECT,
        related_name='pricing_constraints',
        null=True,
        blank=True,
    )
    product_category = models.ForeignKey(
        'ProductCategory',
        verbose_name='Категория продуктов',
        help_text='Указать, если ограничение устанавливается на категорию продуктов',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    product = models.ForeignKey(
        'Product',
        verbose_name='Продукт',
        help_text='Указать, если ограничение устанавливается на конкретный продукт',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    is_active = models.BooleanField(verbose_name='Активно', default=False)
    scope = models.CharField(
        verbose_name='Область действия',
        max_length=20,
        choices=SCOPES,
        default=GLOBAL,
    )
    priority = models.PositiveSmallIntegerField(verbose_name='Приоритет (при пересечениях в scope)')
    max_daily_change_pct = models.PositiveSmallIntegerField(
        verbose_name='Макс. изменение цены за день (в процентах)',
        default=90,
    )
    max_markup_pct = models.PositiveSmallIntegerField(
        verbose_name='Макс. наценка (в процентах)',
        default=1000,
    )

    class Meta:
        verbose_name = 'Ограничение на изменение цены'
        verbose_name_plural = 'Ограничения на изменение цены'

    def __str__(self):
        if self.scope == self.GLOBAL:
            return f'Ограничение №{self.id} глобальное'
        elif self.scope == self.STORAGE:
            return f'Ограничение №{self.id} в хранилище {self.storage}'
        elif self.scope == self.CATEGORY:
            return f'Ограничение №{self.id} по категории {self.product_category}'
        elif self.scope == self.PRODUCT:
            return f'Ограничение №{self.id} на продукт {self.product}'

        return f'Ограничение №{self.id}'


class PricingRun(AutoDateMixin):
    """Приказ на формирование цен в хранилище"""

    STARTED = 'started'
    COMPLETED = 'completed'
    CONFIRMED = 'confirmed'
    FAILED = 'failed'
    STATUSES = {
        STARTED: 'Запущено',
        COMPLETED: 'Завершено',
        CONFIRMED: 'Подтверждено',
        FAILED: 'Ошибка',
    }

    storage = models.ForeignKey(
        'Storage',
        verbose_name='Хранилище',
        on_delete=models.PROTECT,
    )
    created_by = models.ForeignKey(
        'employees.Employee',
        verbose_name='Кем создано',
        on_delete=models.PROTECT,
    )
    status = models.CharField(
        verbose_name='Статус',
        max_length=20,
        choices=STATUSES,
        default=STARTED,
    )
    business_date = models.DateField(verbose_name='Дата, когда приказ действует')
    started_at = models.DateTimeField(verbose_name='Время начала действия')
    finished_at = models.DateTimeField(verbose_name='Время окончания действия', blank=True, null=True)
    confirmed_at = models.DateTimeField(verbose_name='Время подтверждения', blank=True, null=True)
    error_message = models.CharField(verbose_name='Текст ошибки', max_length=300, blank=True, null=True)

    class Meta:
        verbose_name = 'Приказ на формирование цен в хранилище'
        verbose_name_plural = 'Приказы на формирование цен в хранилищах'

    def __str__(self):
        return f'Приказ №{self.id} от {self.business_date}'


class StorePrice(AutoDateMixin):
    """Цена хранилища на день"""

    pricing_run = models.ForeignKey(
        'PricingRun',
        verbose_name='Приказ',
        on_delete=models.PROTECT,
    )
    product = models.ForeignKey(
        'Product',
        verbose_name='Продукт',
        on_delete=models.PROTECT,
    )
    business_date = models.DateField(verbose_name='Дата, когда приказ действует', default=timezone.now)
    price_list_type = models.ForeignKey(
        'PriceListType',
        verbose_name='Тип прайс-листа',
        on_delete=models.PROTECT,
    )
    price_list_base = models.ForeignKey(
        'PriceListBase',
        verbose_name='Основание формирования прайс-листа',
        on_delete=models.PROTECT,
    )
    final_price = models.PositiveSmallIntegerField(verbose_name='Окончательная цена')
    is_sale_allowed = models.BooleanField(verbose_name='Разрешена ли продажа', default=True)
    block_reason = models.CharField(verbose_name='Причина блокировки', default='', blank=True)

    class Meta:
        verbose_name = 'Цена хранилища на день'
        verbose_name_plural = 'Цена хранилища на день'

    def __str__(self):
        return f'Цена №{self.id} для продукта {self.product}'


class CouponDiscountType(AutoDateMixin):
    """Тип скидки в купоне"""

    name = models.CharField(verbose_name='Название', max_length=64, unique=True)

    class Meta:
        verbose_name = 'Тип скидки в купоне'
        verbose_name_plural = 'Типы скидок в купонах'
        ordering = ['name']

    def __str__(self):
        return self.name


class Coupon(AutoDateMixin):
    """Купон"""

    storage = models.ForeignKey(
        'Storage',
        verbose_name='Хранилище',
        on_delete=models.PROTECT,
    )
    product = models.ForeignKey(
        'Product',
        verbose_name='Продукт',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    discount_type = models.ForeignKey(
        'CouponDiscountType',
        verbose_name='Тип скидки',
        on_delete=models.PROTECT,
    )
    value = models.PositiveSmallIntegerField(verbose_name='Размер скидки')
    valid_from = models.DateField(verbose_name='Дата начала действия')
    valid_to = models.DateField(verbose_name='Дата окончания действия')
    min_quantity = models.PositiveSmallIntegerField(
        verbose_name='Мин. кол-во в чеке для применения скидки',
        null=True,
        blank=True,
    )
    is_active = models.BooleanField(verbose_name='Активна', default=False)

    class Meta:
        verbose_name = 'Купон'
        verbose_name_plural = 'Купоны'

    def __str__(self):
        return f'Купон №{self.id} в хранилище {self.storage} c {self.valid_from} по {self.valid_to}'


class PaymentMethod(AutoDateMixin):
    """Тип оплаты"""

    name = models.CharField(verbose_name='Название', max_length=64, unique=True)

    class Meta:
        verbose_name = 'Тип оплаты'
        verbose_name_plural = 'Типы оплаты'
        ordering = ['name']

    def __str__(self):
        return self.name


class SaleReceipt(AutoDateMixin):
    """Чек продажи"""

    DRAFT = 'draft'
    PAID = 'paid'
    CANCELED = 'canceled'
    STATUSES = {
        DRAFT: 'Создан',
        PAID: 'Оплачен',
        CANCELED: 'Отменен',
    }

    storage = models.ForeignKey(
        'Storage',
        verbose_name='Хранилище',
        on_delete=models.PROTECT,
        related_name='receipts',
    )
    cashier = models.ForeignKey(
        'employees.Employee',
        verbose_name='Кассир',
        on_delete=models.PROTECT,
        related_name='cashier_receipts',
    )
    time_session = models.ForeignKey(
        'employees.TimeSession',
        verbose_name='Рабочая сессия',
        on_delete=models.PROTECT,
        related_name='time_session_receipts',
    )
    payment_method = models.ForeignKey(
        'PaymentMethod',
        verbose_name='Тип оплаты',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    status = models.CharField(
        verbose_name='Статус',
        max_length=20,
        choices=STATUSES,
        default=DRAFT,
    )
    opened_at = models.DateTimeField(verbose_name='Время создания')
    closed_at = models.DateTimeField(verbose_name='Время закрытия', null=True, blank=True)
    total_gross = models.PositiveSmallIntegerField(verbose_name='Полная цена')
    total_discount = models.PositiveSmallIntegerField(verbose_name='Размер скидки')
    total_payable = models.PositiveSmallIntegerField(verbose_name='Цена к оплате')
    paid_amount = models.PositiveSmallIntegerField(verbose_name='Оплаченная сумма', null=True, blank=True)
    paid_at = models.DateTimeField(verbose_name='Время оплаты', null=True, blank=True)
    inventory_lots = models.ManyToManyField(
        'InventoryLot',
        through='SalesReceiptLine',
        verbose_name='Партии товара',
        related_name='sale_receipts',
        blank=True,
    )

    class Meta:
        verbose_name = 'Чек продажи'
        verbose_name_plural = 'Чеки продажи'

    def __str__(self):
        return f'Чек №{self.id} в ТТ {self.storage} ({self.cashier}, {self.time_session})'


class SalesReceiptLine(AutoDateMixin):
    """Связка чеки - товары"""

    sale_receipt = models.ForeignKey(
        'SaleReceipt',
        verbose_name='Чек продажи',
        on_delete=models.PROTECT,
    )
    inventory_lot = models.ForeignKey(
        'InventoryLot',
        verbose_name='Партия товара',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    coupon = models.ForeignKey(
        'Coupon',
        verbose_name='Купон',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    price_list_type = models.ForeignKey(
        'PriceListType',
        verbose_name='Тип прайс-листа',
        on_delete=models.PROTECT,
    )
    price_list_base = models.ForeignKey(
        'PriceListBase',
        verbose_name='Основание формирования прайс-листа',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    quantity = models.PositiveSmallIntegerField(verbose_name='Кол-во')
    unit_price = models.PositiveSmallIntegerField(verbose_name='Цена единицы')
    line_discount = models.PositiveSmallIntegerField(verbose_name='Суммарная скидка')
    line_total = models.PositiveSmallIntegerField(verbose_name='Итоговая сумма')

    class Meta:
        verbose_name = 'Связка чеки - товары'
        verbose_name_plural = 'Связки чеки - товары'

    def __str__(self):
        return f'Связка №{self.id} {self.sale_receipt} {self.inventory_lot}'
