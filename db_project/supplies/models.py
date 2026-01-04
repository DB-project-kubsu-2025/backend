from django.db import models

from common_utils.mixins import AutoDateMixin
from supplies.utils import generate_file_path


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


class SupplyContract(AutoDateMixin):
    """Контракт на поставки"""

    supplier = models.ForeignKey(
        'Supplier',
        verbose_name='Поставщик',
        on_delete=models.PROTECT,
        related_name='contracts',
    )
    storage = models.ForeignKey(
        'shops.Storage',
        verbose_name='Хранилище',
        on_delete=models.PROTECT,
    )
    employee_entered_contract = models.ForeignKey(
        'employees.Employee',
        verbose_name='Сотрудник, заключивший договор',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    supplier_contact = models.ForeignKey(
        'SupplyContract',
        verbose_name='Контактное лицо, заключившее договор',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    is_active = models.BooleanField(verbose_name='Активен', default=False)
    expiration_date = models.DateField(verbose_name='Дата истечения договора')

    class Meta:
        verbose_name = 'Договор на поставки'
        verbose_name_plural = 'Договора на поставки'

    def __str__(self):
        return f'Договор №{self.id} {self.supplier.name} - {self.storage.cadastral_number}'


class SupplyContractProduct(AutoDateMixin):
    """Связь продукт - контракт на поставку"""

    ONE_TIME = 'one_time'
    DAILY = 'daily'
    WEEKLY = 'weekly'
    BIWEEKLY = 'biweekly'
    MONTHLY = 'monthly'
    QUARTERLY = 'quarterly'
    ON_DEMAND = 'on_demand'
    FREQUENCY_CHOICES = {
        ONE_TIME: 'Единоразово',
        DAILY: 'Ежедневно',
        WEEKLY: 'Еженедельно',
        BIWEEKLY: 'Раз в две недели',
        MONTHLY: 'Ежемесячно',
        QUARTERLY: 'Ежеквартально',
        ON_DEMAND: 'По требованию',
    }

    supply_contract = models.ForeignKey(
        'SupplyContract',
        verbose_name='Договор на поставку',
        on_delete=models.PROTECT,
        related_name='products',
    )
    product = models.ForeignKey(
        'shops.Product',
        verbose_name='Продукт',
        on_delete=models.PROTECT,
    )
    price = models.PositiveSmallIntegerField(verbose_name='Цена (общая)')
    quantity = models.PositiveSmallIntegerField(verbose_name='Кол-во')
    delivery_frequency = models.CharField(
        verbose_name='Частота доставки',
        max_length=20,
        choices=FREQUENCY_CHOICES,
        default=ONE_TIME,
    )

    class Meta:
        verbose_name = 'Продукт в договоре на поставку'
        verbose_name_plural = 'Продукты в договорах на поставки'

    def __str__(self):
        return f'Контракт №{self.supply_contract.id}: {self.product.name} {self.quantity} {self.delivery_frequency}'


class Supply(AutoDateMixin):
    """Поставка"""

    DRAFT = 'draft'
    IN_RECEIVING = 'in_receiving'
    PENDING_APPROVAL = 'pending_approval'
    APPROVED = 'approved'
    REJECTED = 'rejected'
    CLOSED = 'closed'
    STATUSES = {
        DRAFT: 'Создано',
        IN_RECEIVING: 'Кладовщик вводит фактические данные',
        PENDING_APPROVAL: 'Требует решения товароведа/ГК',
        APPROVED: 'Разрешено проводить',
        REJECTED: 'Отклонено',
        CLOSED: 'Закрыто',
    }

    storage = models.ForeignKey(
        'shops.Storage',
        verbose_name='Хранилище',
        on_delete=models.PROTECT,
    )
    supply_contract = models.ForeignKey(
        'SupplyContract',
        verbose_name='Контракт на поставку',
        on_delete=models.PROTECT,
    )
    created_by = models.ForeignKey(
        'employees.Employee',
        verbose_name='Создана сотрудником',
        on_delete=models.PROTECT,
        related_name='supplies_created',
    )
    received_by = models.ForeignKey(
        'employees.Employee',
        verbose_name='Принята сотрудником',
        on_delete=models.PROTECT,
        related_name='supplies_received',
        null=True,
        blank=True,
    )
    planned_date = models.DateField(verbose_name='Планируемая дата поставки', db_index=True)
    arrived_at = models.DateTimeField(verbose_name='Время прибытия')
    status = models.CharField(
        verbose_name='Статус',
        max_length=20,
        choices=STATUSES,
        default=DRAFT,
    )

    class Meta:
        verbose_name = 'Поставка'
        verbose_name_plural = 'Поставки'
        ordering = ['-planned_date']

    def __str__(self):
        return f'Поставка №{self.id} в {self.storage.cadastral_number} по контракту №{self.supply_contract_id}'


class SupplyProduct(AutoDateMixin):
    """Связка продукт - поставка"""

    OK = 'ok'
    HAS_ISSUES = 'has_issues'
    RESOLVED = 'resolved'
    STATUSES = {
        OK: 'Ок',
        HAS_ISSUES: 'Есть несоответствия',
        RESOLVED: 'Решено',
    }

    supply = models.ForeignKey(
        'Supply',
        verbose_name='Поставка',
        on_delete=models.PROTECT,
    )
    product = models.ForeignKey(
        'shops.Product',
        verbose_name='Продукт',
        on_delete=models.PROTECT,
    )
    supply_contract_product = models.ForeignKey(
        'SupplyContractProduct',
        verbose_name='Продукт в поставке',
        on_delete=models.PROTECT,
    )
    quantity_actual_total = models.PositiveSmallIntegerField(verbose_name='Сумма по связанным партиям')
    quantity_expected = models.PositiveSmallIntegerField(verbose_name='Ожидаемое кол-во')
    requires_review = models.BooleanField(verbose_name='Требует осмотра', default=True)
    status = models.CharField(
        verbose_name='Статус',
        max_length=20,
        choices=STATUSES,
        default=HAS_ISSUES,
    )
    purchase_price = models.PositiveSmallIntegerField(verbose_name='Стоимость покупки')

    class Meta:
        verbose_name = 'Продукт в поставке'
        verbose_name_plural = 'Продукты в поставке'
        ordering = ['status']

    def __str__(self):
        return f'Продукт {self.product.name} в поставке №{self.supply_id}'


class SupplyProductLot(AutoDateMixin):
    """Фактическая партия в продуктах поставки"""

    OK = 'ok'
    DAMAGED = 'damaged'
    CONDITIONS = {
        OK: 'Ок',
        DAMAGED: 'Есть повреждения упаковки',
    }

    DRAFT = 'draft'
    CONFIRMED = 'confirmed'
    ON_HOLD = 'on_hold'
    STATUSES = {
        DRAFT: 'Создано',
        CONFIRMED: 'Подтверждено',
        ON_HOLD: 'На удержании',
    }

    supply_product = models.ForeignKey(
        'SupplyProduct',
        verbose_name='Продукт в поставке',
        on_delete=models.PROTECT,
    )
    manufacture_date = models.DateField(verbose_name='Дата изготовления')
    expiry_date_actual = models.DateField(verbose_name='Фактическая дата окончания срока годности')
    quantity_actual = models.PositiveSmallIntegerField(verbose_name='Фактическое кол-во')
    packaging_condition = models.CharField(
        verbose_name='Состояние упаковки',
        max_length=10,
        choices=CONDITIONS,
    )
    status = models.CharField(
        verbose_name='Статус',
        max_length=10,
        choices=STATUSES,
        default=DRAFT,
    )

    class Meta:
        verbose_name = 'Фактическая партия в продуктах поставки'
        verbose_name_plural = 'Фактические партии в продуктах поставок'
        ordering = ['status']


class DiscrepancyReason(AutoDateMixin):
    """Причина несоответствия поставки ожиданиям"""

    name = models.CharField(verbose_name='Название', max_length=255)

    class Meta:
        verbose_name = 'Причина несоответствия поставки ожиданиям'
        verbose_name_plural = 'Причины несоответствия поставки ожиданиям'

    def __str__(self):
        return self.name


class SupplyDiscrepancy(AutoDateMixin):
    """Несоответствие поставки ожиданиям"""

    OPEN = 'open'
    SENT_TO_HQ = 'sent_to_hq'
    APPROVED = 'approved'
    REJECTED = 'rejected'
    RESOLVED = 'resolved'
    STATUSES = {
        OPEN: 'Открыто',
        SENT_TO_HQ: 'Отправлено в ГК',
        APPROVED: 'Утверждено',
        REJECTED: 'Отклонено',
        RESOLVED: 'Урегулировано',
    }

    supply_product_lot = models.ForeignKey(
        'SupplyProductLot',
        verbose_name='Фактическая партия в продуктах поставки',
        on_delete=models.PROTECT,
    )
    discrepancy_reason = models.ForeignKey(
        'DiscrepancyReason',
        verbose_name='Причина несоответствия поставки ожиданиям',
        on_delete=models.PROTECT,
    )
    created_by = models.ForeignKey(
        'employees.Employee',
        verbose_name='Создано',
        on_delete=models.PROTECT,
        related_name='discrepancies_created',
    )
    decided_by = models.ForeignKey(
        'employees.Employee',
        verbose_name='Принято',
        on_delete=models.PROTECT,
        related_name='discrepancies_decided',
        null=True,
        blank=True,
    )
    comment = models.CharField(verbose_name='Комментарий', max_length=300, default='', blank=True)
    status = models.CharField(
        verbose_name='Статус',
        max_length=20,
        choices=STATUSES,
        default=OPEN,
    )
    decided_at = models.DateTimeField(verbose_name='Дата принятия', null=True, blank=True)
    decision_comment = models.CharField(verbose_name='Комментарий к решению', max_length=300, default='', blank=True)

    class Meta:
        verbose_name = 'Несоответствие поставки ожиданиям'
        verbose_name_plural = 'Несоответствия поставок ожиданиям'
        ordering = ['status']

    def __str__(self):
        return f'Несоответствие №{self.id} (создал {self.created_by}'


class DiscrepancyAttachment(AutoDateMixin):
    """Вложение для несоответствий"""

    supply_discrepancy = models.ForeignKey(
        'SupplyDiscrepancy',
        verbose_name='Заявка на несоответствие поставки',
        on_delete=models.PROTECT,
        related_name='attachments',
    )
    file = models.FileField(
        upload_to=generate_file_path,
        verbose_name='Файл',
    )

    class Meta:
        verbose_name = 'Вложение к заявке на несоответствие поставки'
        verbose_name_plural = 'Вложения к заявкам на несоответствия поставкам'

    def __str__(self):
        return f'Вложение №{self.id} к заявке №{self.supply_discrepancy_id}'
