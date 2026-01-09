from drf_spectacular.utils import OpenApiResponse
from rest_framework import status

MALE = 'male'
FEMALE = 'female'
GENDER_CHOICES = {
    MALE: 'Мужской',
    FEMALE: 'Женский',
}

SIMPLE = 'simple'
FOREIGN = 'foreign'
PASSPORT_TYPES = {
    SIMPLE: 'Обычный',
    FOREIGN: 'Заграничный',
}


class APISchemaTags:
    """Теги АПИ"""

    AUTH_SERVICE = 'Сервис аутентификации'
    EMPLOYEES = 'Работники'
    SUPPLIES = 'Поставки'
    SHOPS = 'Магазины'
    STORAGES = 'Хранилища'
    SPACES = 'Места хранения'
    SUPPLY = 'Поставки'
    PRODUCTS = 'Продукты'
    ML_SERVICE = 'АПИ для ml_service'
    CATEGORIES = 'Категории продуктов'
    DISCOUNT_TYPES = 'Типы скидок'
    MOVEMENT_TYPES = 'Типы перемещений'
    PAYMENT_TYPES = 'Типы оплаты'
    PRICE_LISTS = 'Прайс-листы'
    STOP_LISTS = 'Стоп-листы'
    INVENTORY = 'Инвентаризация'
    WRITEOFF = 'Списания'
    PRODUCT_UNITS = 'Единицы измерения'
    PRODUCT_CATEGORIES = 'Категории продуктов'
    STORAGE_PROFILES = 'Профили хранения'
    PRODUCT_MEDIA = 'Медиа продуктов'
    PRODUCT_INVENTORY_LOTS = 'Партии товаров'
    STORAGE_TYPES = 'Типы хранилищ'
    INVENTORY_BALANCE = 'Остатки инвентаря'
    INVENTORY_MOVEMENTS = 'Перемещения инвентаря'
    PRICE_LIST_PRODUCTS = 'Продукты прайс-листов'
    PRICING_CONSTRAINTS = 'Ограничения ценообразования'
    PRICING_RUNS = 'Запуски ценообразования'
    STORE_PRICES = 'Цены магазинов'
    COUPONS = 'Купоны'
    SALE_RECEIPTS = 'Чеки продаж'
    SALES_RECEIPT_LINES = 'Строки чеков'
    STOP_LIST_PRODUCTS = 'Продукты стоп-листов'
    STOCK_TAKES = 'Инвентаризации'
    STOCK_TAKE_LINES = 'Строки инвентаризации'
    STOCK_TAKE_ADJUSTMENTS = 'Корректировки инвентаризации'
    WRITE_OFF_ACTS = 'Акты списания'
    WRITEOFF_LINES = 'Строки списания'
    WRITEOFF_ATTACHMENTS = 'Вложения списания'
    WRITEOFF_POSTINGS = 'Проводки списания'


class DefaultAPIResponses:
    """Ответы сервера по умолчанию"""

    _success_text = 'Стандартный ответ при успешном ответе'
    _bad_request_error_text = 'Описание ошибки валидации'
    _unauthorized_error_text = 'Учетные данные не были предоставлены'
    _access_denied = 'У вас нет прав на выполнение этого действия'
    _not_found_error_text = 'Страница не найдена'
    _method_not_allowed_error_text = 'Метод <method> не разрешён для этого ресурса'
    _internal_server_error_text = 'Произошла внутренняя ошибка сервера'

    RESPONSES = {
        status.HTTP_400_BAD_REQUEST: OpenApiResponse(
            description=_bad_request_error_text
        ),
        status.HTTP_401_UNAUTHORIZED: OpenApiResponse(
            description=_unauthorized_error_text
        ),
        status.HTTP_403_FORBIDDEN: OpenApiResponse(description=_access_denied),
        status.HTTP_404_NOT_FOUND: OpenApiResponse(description=_not_found_error_text),
        status.HTTP_405_METHOD_NOT_ALLOWED: OpenApiResponse(
            description=_method_not_allowed_error_text
        ),
        status.HTTP_500_INTERNAL_SERVER_ERROR: OpenApiResponse(
            description=_internal_server_error_text
        ),
    }
