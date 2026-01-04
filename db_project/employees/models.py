from django.contrib.auth.models import AbstractUser
from django.db import models

from common_utils import constants
from common_utils.mixins import AutoDateMixin
from employees.constants import LeaveRequestStatus
from employees.utils import generate_file_path


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


class WorkingRate(AutoDateMixin):
    """Рабочая ставка"""

    name = models.CharField(verbose_name='Название', unique=True)
    monthly_output = models.PositiveSmallIntegerField(verbose_name='Рабочая выработка (в часах)')

    class Meta:
        verbose_name = 'Рабочая ставка'
        verbose_name_plural = 'Справочник рабочих ставок'

    def __str__(self):
        return f'{self.name} - {self.monthly_output}'


class JobPosition(AutoDateMixin):
    """Должность"""

    name = models.CharField(verbose_name='Название', max_length=100, unique=True)

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Справочник должностей'
        ordering = ['name']

    def __str__(self):
        return self.name


class Salary(AutoDateMixin):
    """Зарплата"""

    amount = models.PositiveSmallIntegerField(verbose_name='Сумма')
    job_position = models.ForeignKey(
        'JobPosition',
        verbose_name='Должность',
        on_delete=models.PROTECT,
        related_name='salaries',
    )
    working_rate = models.ForeignKey(
        'WorkingRate',
        verbose_name='Ставка',
        on_delete=models.PROTECT,
        related_name='salaries',
    )

    class Meta:
        verbose_name = 'Зарплата на должности'
        verbose_name_plural = 'Зарплаты на должности'

    def __str__(self):
        return f'{self.id} -> {self.amount}'


class Workplace(AutoDateMixin):
    """Рабочее место"""

    # сотрудник может работать либо в хранилище, либо в филиале ГК
    storage = models.ForeignKey(
        'shops.Storage',
        verbose_name='Хранилище',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    main_office_filial = models.ForeignKey(
        'offices.MainOfficeFilial',
        verbose_name='Филиал ГК',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'Рабочее место'
        verbose_name_plural = 'Рабочие места'

    def __str__(self):
        return f'Рабоче место №{self.id}'


class Employee(AbstractUser, AutoDateMixin):
    """Модель: Работник"""

    workplace = models.OneToOneField(
        'Workplace',
        verbose_name='Рабочее место',
        help_text='Пустое, если работник не работает',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
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


class LeaveRequestType(AutoDateMixin):
    """Тип запроса на временное отсутствие"""

    name = models.CharField(verbose_name='Название', max_length=60)
    counts_against_annual = models.BooleanField(verbose_name='Учитывается в годовом исчислении', default=False)
    requires_documents = models.BooleanField(verbose_name='Требует документы', default=False)
    documents_due_days = models.PositiveSmallIntegerField(verbose_name='Сроки сдачи документов', null=True, blank=True)

    class Meta:
        verbose_name = 'Тип запроса на временное отсутствие'
        verbose_name_plural = 'Типы запросов на временное отсутствие'
        ordering = ['name']

    def __str__(self):
        return self.name


class LeaveRequest(AutoDateMixin):
    """Запрос на временное отсутствие"""

    employee = models.ForeignKey(
        'Employee',
        verbose_name='Работник',
        on_delete=models.PROTECT,
        related_name='leave_requests',
    )
    approved_by = models.ForeignKey(
        'Employee',
        verbose_name='Сотрудник, одобривший запрос',
        help_text='Пустое, если запрос не одобрен',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    status = models.CharField(
        verbose_name='Статус',
        choices=LeaveRequestStatus.STATUSES,
        max_length=30,
        db_index=True,
    )
    start_date = models.DateField(verbose_name='Дата начала')
    end_date = models.DateField(verbose_name='Дата окончания')
    approved_at = models.DateTimeField(verbose_name='Дата подтверждения', null=True, blank=True)
    comment = models.CharField(verbose_name='Комментарий', max_length=300, blank=True, default='')
    documents_received_at = models.DateTimeField(
        verbose_name='Документы были предоставлены в',
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'Запрос на временное отсутствие'
        verbose_name_plural = 'Запросы на временное отсутствие'
        ordering = ['start_date', 'end_date']

    def __str__(self):
        return f'{self.id}: {self.start_date} - {self.end_date}'


class LeaveRequestAttachment(AutoDateMixin):
    """Приложение к запросу на временное отсутствие"""

    leave_request = models.ForeignKey(
        'LeaveRequest',
        verbose_name='Запрос на временное отсутствие',
        on_delete=models.PROTECT,
        related_name='attachments',
    )
    file = models.FileField(
        verbose_name='Файл',
        upload_to=generate_file_path,
    )

    class Meta:
        verbose_name = 'Приложение к запросу на отсутствие'
        verbose_name_plural = 'Приложения к запросам на отсутствие'

    def __str__(self):
        return f'Приложение для {self.leave_request_id}'


class AnnualLeaveBalance(AutoDateMixin):
    """Отпускной баланс по годам"""

    employee = models.ForeignKey(
        'Employee',
        verbose_name='Работник',
        on_delete=models.PROTECT,
        related_name='annual_leave_balances',
    )
    year = models.PositiveSmallIntegerField(verbose_name='Год', db_index=True)
    base_days = models.PositiveSmallIntegerField(verbose_name='Число дней отпуска', default=28)
    carry_in_days = models.PositiveSmallIntegerField(verbose_name='Переноска в дни', default=0)
    manual_adjust_days = models.PositiveSmallIntegerField(verbose_name='Ручная корректировка дней', default=0)

    class Meta:
        verbose_name = 'Отпускной баланс по годам'
        verbose_name_plural = 'Отпускные балансы по годам'

    def __str__(self):
        return f'Работник {self.employee_id} -> {self.year}'


class GlobalTimePolicy(AutoDateMixin):
    """Единая политика рабочего времени"""

    required_minutes = models.PositiveSmallIntegerField(verbose_name='Необходимые минуты')
    cut_off_minute = models.PositiveSmallIntegerField(verbose_name='Отсекаемая минута')
    prompt_wait_minutes = models.PositiveSmallIntegerField(verbose_name='Минуты ожидания', default=5)
    effective_from = models.DateField(verbose_name='Действует с')
    effective_to = models.DateField(verbose_name='Действует до')

    class Meta:
        verbose_name = 'Единая политика рабочего времени'
        verbose_name_plural = 'Единые политики рабочего времени'

    def __str__(self):
        return f'Единая политика рабочего времени с {self.effective_from} до {self.effective_to}'


class TimeWorkType(AutoDateMixin):
    """Тип работ для списания времени"""

    name = models.CharField(verbose_name='Название', max_length=80)
    is_active = models.BooleanField(verbose_name='Активность', default=True)

    class Meta:
        verbose_name = 'Тип работ для списания времени'
        verbose_name_plural = 'Типы работ для списания времени'
        ordering = ['name']

    def __str__(self):
        return self.name


class TimeEntry(AutoDateMixin):
    """Списание времени"""

    employee = models.ForeignKey(
        'Employee',
        verbose_name='Работник',
        on_delete=models.PROTECT,
        related_name='time_entries',
    )
    work_type = models.ForeignKey(
        'TimeWorkType',
        verbose_name='Тип работ',
        on_delete=models.PROTECT,
    )
    date = models.DateField(verbose_name='Дата', db_index=True)
    minutes = models.PositiveSmallIntegerField(verbose_name='Минуты')
    comment = models.CharField(verbose_name='Комментарий', max_length=300, blank=True, default='')

    class Meta:
        verbose_name = 'Списание времени'
        verbose_name_plural = 'Списания времени'

    def __str__(self):
        return f'Списания времени для работника {self.employee_id} за {self.date} в {self.minutes} мин.'


class TimeSessionCloseReason(AutoDateMixin):
    """Причина закрытия рабочей сессии"""

    name = models.CharField(verbose_name='Название', max_length=80)

    class Meta:
        verbose_name = 'Причина закрытия рабочей сессии'
        verbose_name_plural = 'Причины закрытия рабочей сессии'
        ordering = ['name']


class TimeSession(AutoDateMixin):
    """Рабочая сессия"""

    employee = models.ForeignKey(
        'Employee',
        verbose_name='Работник',
        on_delete=models.PROTECT,
        related_name='time_sessions',
    )
    close_reason = models.ForeignKey(
        'TimeSessionCloseReason',
        verbose_name='Причина закрытия сессии',
        help_text='Заполняется только если сессия была закрыта',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    closed = models.BooleanField(verbose_name='Закрыта', default=False, db_index=True)
    login_at = models.DateTimeField(verbose_name='Время начала')
    logout_at = models.DateTimeField(verbose_name='Время окончания', null=True, blank=True)

    class Meta:
        verbose_name = 'Рабочая сессия'
        verbose_name_plural = 'Рабочие сессии'

    def __str__(self):
        return f'Рабочая сессия работника {self.employee_id}: {self.login_at}'


class AdjustmentReason(AutoDateMixin):
    """Причина корректировки"""

    name = models.CharField(verbose_name='Название', max_length=80)

    class Meta:
        verbose_name = 'Причина корректировки'
        verbose_name_plural = 'Причины корректировки'
        ordering = ['name']

    def __str__(self):
        return self.name


class TimeDay(AutoDateMixin):
    """Сводка по дню сотрудника"""

    employee = models.ForeignKey(
        'Employee',
        verbose_name='Работник',
        on_delete=models.PROTECT,
        related_name='time_days',
    )
    date = models.DateField(verbose_name='Дата', db_index=True)
    comment = models.CharField(verbose_name='Комментарий', max_length=300, blank=True, default='')
    adjusted_minutes = models.PositiveSmallIntegerField(verbose_name='Скорректированные минуты', default=0, blank=True)
    adjustment_reason = models.ForeignKey(
        'AdjustmentReason',
        verbose_name='Причина корректировки',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'Сводка по дню сотрудника'
        verbose_name_plural = 'Сводки по дням сотрудника'

    def __str__(self):
        return f'Сводка по дню работника {self.employee_id} за {self.date}'
