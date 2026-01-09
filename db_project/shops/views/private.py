from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from common_utils.constants import APISchemaTags, DefaultAPIResponses
from common_utils.permissions import (
    HasStorekeeperGroupPermission,
    HasCommodityExpertGroupPermission,
    HasMainOfficeGroupPermission, HasSellerGroupPermission,
)
from shops.models import Space, InventoryLot, Storage, ProductMedia, InventoryBalance, InventoryMovement, \
    PriceList, PriceListProduct, PricingConstraint, PricingRun, StorePrice, Coupon, SaleReceipt, SalesReceiptLine, \
    StopList, StopListProduct, StockTake, StockTakeLine, StockTakeAdjustment, WriteOffAct, WriteoffLine, \
    WriteoffAttachment, WriteoffPosting, ProductInventoryLot
from shops.serializers import (
    SpaceRequestSerializer,
    InventoryLotRequestSerializer,
    StorageRequestSerializer,
    ProductMediaRequestSerializer,
    InventoryBalanceResponseSerializer,
    InventoryBalanceRequestSerializer,
    InventoryMovementResponseSerializer,
    InventoryMovementRequestSerializer,
    PriceListResponseSerializer,
    PriceListRequestSerializer,
    PriceListProductResponseSerializer,
    PriceListProductRequestSerializer,
    PricingConstraintResponseSerializer,
    PricingConstraintRequestSerializer,
    PricingRunResponseSerializer,
    PricingRunRequestSerializer,
    StorePriceResponseSerializer,
    StorePriceRequestSerializer,
    CouponResponseSerializer,
    CouponRequestSerializer,
    SaleReceiptResponseSerializer,
    SaleReceiptRequestSerializer,
    SalesReceiptLineResponseSerializer,
    SalesReceiptLineRequestSerializer,
    StopListResponseSerializer,
    StopListRequestSerializer,
    StopListProductResponseSerializer,
    StopListProductRequestSerializer,
    StockTakeResponseSerializer,
    StockTakeRequestSerializer,
    StockTakeLineResponseSerializer,
    StockTakeLineRequestSerializer,
    StockTakeAdjustmentResponseSerializer,
    StockTakeAdjustmentRequestSerializer,
    WriteOffActResponseSerializer,
    WriteOffActRequestSerializer,
    WriteoffLineResponseSerializer,
    WriteoffLineRequestSerializer,
    WriteoffAttachmentResponseSerializer,
    WriteoffAttachmentRequestSerializer,
    WriteoffPostingResponseSerializer,
    WriteoffPostingRequestSerializer,
    ProductInventoryLotRequestSerializer, ProductInventoryLotResponseSerializer, StorageResponseSerializer,
    ProductMediaResponseSerializer, InventoryLotResponseSerializer, SpaceResponseSerializer,
)


@extend_schema_view(
    create=extend_schema(
        summary="Создать хранилище",
        description='Создание нового хранилища',
        tags=[APISchemaTags.STORAGES],
        request=StorageRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_201_CREATED: StorageRequestSerializer,
        },
    ),
    list=extend_schema(
        summary="Получить список хранилищ",
        description='Возвращает полный список всех хранилищ',
        tags=[APISchemaTags.STORAGES],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: StorageRequestSerializer(many=True),
        },
    ),
    retrieve=extend_schema(
        summary="Получить хранилище по ID",
        description="Возвращает детальную информацию о конкретном хранилище",
        tags=[APISchemaTags.STORAGES],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID хранилища',
                required=True,
                type=int,
                location=OpenApiParameter.PATH,
            ),
        ],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: StorageRequestSerializer,
        },
    ),
    update=extend_schema(
        summary="Обновить хранилище",
        description='Полное обновление информации о хранилище',
        tags=[APISchemaTags.STORAGES],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID хранилища',
                required=True,
                type=int,
                location=OpenApiParameter.PATH
            ),
        ],
        request=StorageRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: StorageRequestSerializer,
        },
    ),
    partial_update=extend_schema(
        summary="Частично обновить хранилище",
        description='Частичное обновление информации о хранилище',
        tags=[APISchemaTags.STORAGES],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID хранилища',
                required=True,
                type=int,
                location=OpenApiParameter.PATH
            ),
        ],
        request=StorageRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: StorageRequestSerializer,
        },
    ),
    destroy=extend_schema(
        summary="Удалить хранилище",
        description='Удаление хранилища из системы',
        tags=[APISchemaTags.STORAGES],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID хранилища',
                required=True,
                type=int,
                location=OpenApiParameter.PATH
            ),
        ],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_204_NO_CONTENT: None,
        },
    ),
)
class StorageViewSet(viewsets.ModelViewSet):
    """CRUD операции для хранилищ"""

    permission_classes = [IsAuthenticated, HasMainOfficeGroupPermission]
    authentication_classes = [JWTAuthentication]
    queryset = Storage.objects.all()
    serializer_class = StorageResponseSerializer
    lookup_field = 'id'


@extend_schema_view(
    create=extend_schema(
        summary="Создать медиа для товара",
        description='Создание нового медиа для карточки товара',
        tags=[APISchemaTags.PRODUCTS],
        request=ProductMediaRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_201_CREATED: ProductMediaRequestSerializer,
        },
    ),
    list=extend_schema(
        summary="Получить список медиа товаров",
        description='Возвращает список медиа для карточек товаров с фильтрацией по product_id',
        tags=[APISchemaTags.PRODUCTS],
        parameters=[
            OpenApiParameter(
                name='product_id',
                description='Фильтр по ID продукта',
                required=False,
                type=int,
                location=OpenApiParameter.QUERY
            ),
        ],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: ProductMediaRequestSerializer(many=True),
        },
    ),
    retrieve=extend_schema(
        summary="Получить медиа товара по ID",
        description="Возвращает детальную информацию о конкретном медиа товара",
        tags=[APISchemaTags.PRODUCTS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID медиа товара',
                required=True,
                type=int,
                location=OpenApiParameter.PATH
            ),
        ],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: ProductMediaRequestSerializer,
        },
    ),
    update=extend_schema(
        summary="Обновить медиа товара",
        description='Полное обновление информации о медиа товара',
        tags=[APISchemaTags.PRODUCTS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID медиа товара',
                required=True,
                type=int,
                location=OpenApiParameter.PATH
            ),
        ],
        request=ProductMediaRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: ProductMediaRequestSerializer,
        },
    ),
    partial_update=extend_schema(
        summary="Частично обновить медиа товара",
        description='Частичное обновление информации о медиа товара',
        tags=[APISchemaTags.PRODUCTS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID медиа товара',
                required=True,
                type=int,
                location=OpenApiParameter.PATH
            ),
        ],
        request=ProductMediaRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: ProductMediaRequestSerializer,
        },
    ),
    destroy=extend_schema(
        summary="Удалить медиа товара",
        description='Удаление медиа товара из системы',
        tags=[APISchemaTags.PRODUCTS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID медиа товара',
                required=True,
                type=int,
                location=OpenApiParameter.PATH
            ),
        ],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_204_NO_CONTENT: None,
        },
    ),
)
class ProductMediaViewSet(viewsets.ModelViewSet):
    """CRUD операции для медиа товаров"""

    permission_classes = [IsAuthenticated, HasMainOfficeGroupPermission]
    authentication_classes = [JWTAuthentication]
    queryset = ProductMedia.objects.all()
    serializer_class = ProductMediaResponseSerializer
    lookup_field = 'id'

    def get_queryset(self):
        queryset = super().get_queryset()
        product_id = self.request.query_params.get('product_id')
        if product_id:
            queryset = queryset.filter(product_id=product_id)
        return queryset


@extend_schema_view(
    create=extend_schema(
        summary="Создать место хранения",
        description='Создание нового места хранения в хранилище',
        tags=[APISchemaTags.STORAGES],
        request=SpaceRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_201_CREATED: SpaceRequestSerializer,
        },
    ),
    list=extend_schema(
        summary="Получить список мест хранения",
        description='Возвращает полный список всех мест хранения',
        tags=[APISchemaTags.STORAGES],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: SpaceRequestSerializer(many=True),
        },
    ),
    retrieve=extend_schema(
        summary="Получить место хранения по ID",
        description="Возвращает детальную информацию о конкретном месте хранения",
        tags=[APISchemaTags.STORAGES],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID места хранения',
                required=True,
                type=int,
                location=OpenApiParameter.PATH
            ),
        ],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: SpaceRequestSerializer,
        },
    ),
    update=extend_schema(
        summary="Обновить место хранения",
        description='Полное обновление информации о месте хранения',
        tags=[APISchemaTags.STORAGES],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID места хранения',
                required=True,
                type=int,
                location=OpenApiParameter.PATH
            ),
        ],
        request=SpaceRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: SpaceRequestSerializer,
        },
    ),
    partial_update=extend_schema(
        summary="Частично обновить место хранения",
        description='Частичное обновление информации о месте хранения',
        tags=[APISchemaTags.STORAGES],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID места хранения',
                required=True,
                type=int,
                location=OpenApiParameter.PATH
            ),
        ],
        request=SpaceRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: SpaceRequestSerializer,
        },
    ),
    destroy=extend_schema(
        summary="Удалить место хранения",
        description='Удаление места хранения из системы',
        tags=[APISchemaTags.STORAGES],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID места хранения',
                required=True,
                type=int,
                location=OpenApiParameter.PATH
            ),
        ],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_204_NO_CONTENT: None,
        },
    ),
)
class SpaceViewSet(viewsets.ModelViewSet):
    """CRUD операции для мест хранения"""

    authentication_classes = [JWTAuthentication]
    queryset = Space.objects.all()
    serializer_class = SpaceResponseSerializer
    lookup_field = 'id'

    def get_permissions(self):
        """Настроить права доступа в зависимости от действия"""
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated, HasStorekeeperGroupPermission]
        return [permission() for permission in permission_classes]


@extend_schema_view(
    create=extend_schema(
        summary="Создать партию товара",
        description='Создание новой партии товара',
        tags=[APISchemaTags.SUPPLY],
        request=InventoryLotRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_201_CREATED: InventoryLotRequestSerializer,
        },
    ),
    list=extend_schema(
        summary="Получить список партий товара",
        description='Возвращает полный список всех партий товаров',
        tags=[APISchemaTags.SUPPLY],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: InventoryLotRequestSerializer(many=True),
        },
    ),
    retrieve=extend_schema(
        summary="Получить партию товара по ID",
        description="Возвращает детальную информацию о конкретной партии товара",
        tags=[APISchemaTags.SUPPLY],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID партии товара',
                required=True,
                type=int,
                location=OpenApiParameter.PATH
            ),
        ],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: InventoryLotRequestSerializer,
        },
    ),
    update=extend_schema(
        summary="Обновить партию товара",
        description='Полное обновление информации о партии товара',
        tags=[APISchemaTags.SUPPLY],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID партии товара',
                required=True,
                type=int,
                location=OpenApiParameter.PATH
            ),
        ],
        request=InventoryLotRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: InventoryLotRequestSerializer,
        },
    ),
    partial_update=extend_schema(
        summary="Частично обновить партию товара",
        description='Частичное обновление информации о партии товара',
        tags=[APISchemaTags.SUPPLY],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID партии товара',
                required=True,
                type=int,
                location=OpenApiParameter.PATH
            ),
        ],
        request=InventoryLotRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: InventoryLotRequestSerializer,
        },
    ),
    destroy=extend_schema(
        summary="Удалить партию товара",
        description='Удаление партии товара из системы',
        tags=[APISchemaTags.SUPPLY],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID партии товара',
                required=True,
                type=int,
                location=OpenApiParameter.PATH
            ),
        ],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_204_NO_CONTENT: None,
        },
    ),
)
class InventoryLotViewSet(viewsets.ModelViewSet):
    """CRUD операции для партий товаров"""

    permission_classes = [IsAuthenticated, HasCommodityExpertGroupPermission]
    authentication_classes = [JWTAuthentication]
    queryset = InventoryLot.objects.all()
    serializer_class = InventoryLotResponseSerializer
    lookup_field = 'id'


@extend_schema_view(
    create=extend_schema(
        summary='Создать баланс инвентаря',
        description='Создание новой записи о балансе инвентаря',
        tags=[APISchemaTags.INVENTORY_BALANCE],
        request=InventoryBalanceRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_201_CREATED: InventoryBalanceResponseSerializer,
        },
    ),
    list=extend_schema(
        summary='Получить список балансов инвентаря',
        description='Возвращает полный список всех балансов инвентаря',
        tags=[APISchemaTags.INVENTORY_BALANCE],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: InventoryBalanceResponseSerializer(many=True),
        },
    ),
    retrieve=extend_schema(
        summary='Получить баланс инвентаря по ID',
        description='Возвращает детальную информацию о конкретном балансе инвентаря',
        tags=[APISchemaTags.INVENTORY_BALANCE],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID баланса инвентаря',
                required=True,
                type=int,
                location=OpenApiParameter.PATH,
            ),
        ],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: InventoryBalanceResponseSerializer,
        },
    ),
    update=extend_schema(
        summary='Обновить баланс инвентаря',
        description='Полное обновление информации о балансе инвентаря',
        tags=[APISchemaTags.INVENTORY_BALANCE],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID баланса инвентаря',
                required=True,
                type=int,
                location=OpenApiParameter.PATH,
            ),
        ],
        request=InventoryBalanceRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: InventoryBalanceResponseSerializer,
        },
    ),
    partial_update=extend_schema(
        summary='Частично обновить баланс инвентаря',
        description='Частичное обновление информации о балансе инвентаря',
        tags=[APISchemaTags.INVENTORY_BALANCE],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID баланса инвентаря',
                required=True,
                type=int,
                location=OpenApiParameter.PATH,
            ),
        ],
        request=InventoryBalanceRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: InventoryBalanceResponseSerializer,
        },
    ),
    destroy=extend_schema(
        summary='Удалить баланс инвентаря',
        description='Удаление баланса инвентаря из системы',
        tags=[APISchemaTags.INVENTORY_BALANCE],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID баланса инвентаря',
                required=True,
                type=int,
                location=OpenApiParameter.PATH,
            ),
        ],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_204_NO_CONTENT: None,
        },
    ),
)
class InventoryBalanceViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, HasStorekeeperGroupPermission]
    authentication_classes = [JWTAuthentication]
    queryset = InventoryBalance.objects.all()
    serializer_class = InventoryBalanceResponseSerializer
    lookup_field = 'id'


@extend_schema_view(
    create=extend_schema(
        summary='Создать перемещение инвентаря',
        description='Создание нового перемещения инвентаря',
        tags=[APISchemaTags.INVENTORY_MOVEMENTS],
        request=InventoryMovementRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_201_CREATED: InventoryMovementResponseSerializer,
        },
    ),
    list=extend_schema(
        summary='Получить список перемещений инвентаря',
        description='Возвращает полный список всех перемещений инвентаря',
        tags=[APISchemaTags.INVENTORY_MOVEMENTS],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: InventoryMovementResponseSerializer(many=True),
        },
    ),
    retrieve=extend_schema(
        summary='Получить перемещение инвентаря по ID',
        description='Возвращает детальную информацию о конкретном перемещении инвентаря',
        tags=[APISchemaTags.INVENTORY_MOVEMENTS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID перемещения инвентаря',
                required=True,
                type=int,
                location=OpenApiParameter.PATH,
            ),
        ],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: InventoryMovementResponseSerializer,
        },
    ),
    update=extend_schema(
        summary='Обновить перемещение инвентаря',
        description='Полное обновление информации о перемещении инвентаря',
        tags=[APISchemaTags.INVENTORY_MOVEMENTS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID перемещения инвентаря',
                required=True,
                type=int,
                location=OpenApiParameter.PATH,
            ),
        ],
        request=InventoryMovementRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: InventoryMovementResponseSerializer,
        },
    ),
    partial_update=extend_schema(
        summary='Частично обновить перемещение инвентаря',
        description='Частичное обновление информации о перемещении инвентаря',
        tags=[APISchemaTags.INVENTORY_MOVEMENTS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID перемещения инвентаря',
                required=True,
                type=int,
                location=OpenApiParameter.PATH,
            ),
        ],
        request=InventoryMovementRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: InventoryMovementResponseSerializer,
        },
    ),
    destroy=extend_schema(
        summary='Удалить перемещение инвентаря',
        description='Удаление перемещения инвентаря из системы',
        tags=[APISchemaTags.INVENTORY_MOVEMENTS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID перемещения инвентаря',
                required=True,
                type=int,
                location=OpenApiParameter.PATH,
            ),
        ],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_204_NO_CONTENT: None,
        },
    ),
)
class InventoryMovementViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, HasStorekeeperGroupPermission]
    authentication_classes = [JWTAuthentication]
    queryset = InventoryMovement.objects.all()
    serializer_class = InventoryMovementResponseSerializer
    lookup_field = 'id'


@extend_schema_view(
    create=extend_schema(
        summary='Создать прайс-лист',
        description='Создание нового прайс-листа',
        tags=[APISchemaTags.PRICE_LISTS],
        request=PriceListRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_201_CREATED: PriceListResponseSerializer,
        },
    ),
    list=extend_schema(
        summary='Получить список прайс-листов',
        description='Возвращает полный список всех прайс-листов',
        tags=[APISchemaTags.PRICE_LISTS],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: PriceListResponseSerializer(many=True),
        },
    ),
    retrieve=extend_schema(
        summary='Получить прайс-лист по ID',
        description='Возвращает детальную информацию о конкретном прайс-листе',
        tags=[APISchemaTags.PRICE_LISTS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID прайс-листа',
                required=True,
                type=int,
                location=OpenApiParameter.PATH,
            ),
        ],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: PriceListResponseSerializer,
        },
    ),
    update=extend_schema(
        summary='Обновить прайс-лист',
        description='Полное обновление информации о прайс-листе',
        tags=[APISchemaTags.PRICE_LISTS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID прайс-листа',
                required=True,
                type=int,
                location=OpenApiParameter.PATH,
            ),
        ],
        request=PriceListRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: PriceListResponseSerializer,
        },
    ),
    partial_update=extend_schema(
        summary='Частично обновить прайс-лист',
        description='Частичное обновление информации о прайс-листе',
        tags=[APISchemaTags.PRICE_LISTS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID прайс-листа',
                required=True,
                type=int,
                location=OpenApiParameter.PATH,
            ),
        ],
        request=PriceListRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: PriceListResponseSerializer,
        },
    ),
    destroy=extend_schema(
        summary='Удалить прайс-лист',
        description='Удаление прайс-листа из системы',
        tags=[APISchemaTags.PRICE_LISTS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID прайс-листа',
                required=True,
                type=int,
                location=OpenApiParameter.PATH,
            ),
        ],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_204_NO_CONTENT: None,
        },
    ),
)
class PriceListViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, HasMainOfficeGroupPermission]
    authentication_classes = [JWTAuthentication]
    queryset = PriceList.objects.all()
    serializer_class = PriceListResponseSerializer
    lookup_field = 'id'


@extend_schema_view(
    create=extend_schema(
        summary='Создать продукт прайс-листа',
        description='Создание нового продукта прайс-листа',
        tags=[APISchemaTags.PRICE_LIST_PRODUCTS],
        request=PriceListProductRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_201_CREATED: PriceListProductResponseSerializer,
        },
    ),
    list=extend_schema(
        summary='Получить список продуктов прайс-листов',
        description='Возвращает полный список всех продуктов прайс-листов',
        tags=[APISchemaTags.PRICE_LIST_PRODUCTS],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: PriceListProductResponseSerializer(many=True),
        },
    ),
    retrieve=extend_schema(
        summary='Получить продукт прайс-листа по ID',
        description='Возвращает детальную информацию о конкретном продукте прайс-листа',
        tags=[APISchemaTags.PRICE_LIST_PRODUCTS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID продукта прайс-листа',
                required=True,
                type=int,
                location=OpenApiParameter.PATH,
            ),
        ],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: PriceListProductResponseSerializer,
        },
    ),
    update=extend_schema(
        summary='Обновить продукт прайс-листа',
        description='Полное обновление информации о продукте прайс-листа',
        tags=[APISchemaTags.PRICE_LIST_PRODUCTS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID продукта прайс-листа',
                required=True,
                type=int,
                location=OpenApiParameter.PATH,
            ),
        ],
        request=PriceListProductRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: PriceListProductResponseSerializer,
        },
    ),
    partial_update=extend_schema(
        summary='Частично обновить продукт прайс-листа',
        description='Частичное обновление информации о продукте прайс-листа',
        tags=[APISchemaTags.PRICE_LIST_PRODUCTS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID продукта прайс-листа',
                required=True,
                type=int,
                location=OpenApiParameter.PATH,
            ),
        ],
        request=PriceListProductRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: PriceListProductResponseSerializer,
        },
    ),
    destroy=extend_schema(
        summary='Удалить продукт прайс-листа',
        description='Удаление продукта прайс-листа из системы',
        tags=[APISchemaTags.PRICE_LIST_PRODUCTS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID продукта прайс-листа',
                required=True,
                type=int,
                location=OpenApiParameter.PATH,
            ),
        ],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_204_NO_CONTENT: None,
        },
    ),
)
class PriceListProductViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, HasMainOfficeGroupPermission]
    authentication_classes = [JWTAuthentication]
    queryset = PriceListProduct.objects.all()
    serializer_class = PriceListProductResponseSerializer
    lookup_field = 'id'


@extend_schema_view(
    create=extend_schema(
        summary='Создать ограничение ценообразования',
        description='Создание нового ограничения ценообразования',
        tags=[APISchemaTags.PRICING_CONSTRAINTS],
        request=PricingConstraintRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_201_CREATED: PricingConstraintResponseSerializer,
        },
    ),
    list=extend_schema(
        summary='Получить список ограничений ценообразования',
        description='Возвращает полный список всех ограничений ценообразования',
        tags=[APISchemaTags.PRICING_CONSTRAINTS],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: PricingConstraintResponseSerializer(many=True),
        },
    ),
    retrieve=extend_schema(
        summary='Получить ограничение ценообразования по ID',
        description='Возвращает детальную информацию о конкретном ограничении ценообразования',
        tags=[APISchemaTags.PRICING_CONSTRAINTS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID ограничения ценообразования',
                required=True,
                type=int,
                location=OpenApiParameter.PATH,
            ),
        ],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: PricingConstraintResponseSerializer,
        },
    ),
    update=extend_schema(
        summary='Обновить ограничение ценообразования',
        description='Полное обновление информации об ограничении ценообразования',
        tags=[APISchemaTags.PRICING_CONSTRAINTS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID ограничения ценообразования',
                required=True,
                type=int,
                location=OpenApiParameter.PATH,
            ),
        ],
        request=PricingConstraintRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: PricingConstraintResponseSerializer,
        },
    ),
    partial_update=extend_schema(
        summary='Частично обновить ограничение ценообразования',
        description='Частичное обновление информации об ограничении ценообразования',
        tags=[APISchemaTags.PRICING_CONSTRAINTS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID ограничения ценообразования',
                required=True,
                type=int,
                location=OpenApiParameter.PATH,
            ),
        ],
        request=PricingConstraintRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: PricingConstraintResponseSerializer,
        },
    ),
    destroy=extend_schema(
        summary='Удалить ограничение ценообразования',
        description='Удаление ограничения ценообразования из системы',
        tags=[APISchemaTags.PRICING_CONSTRAINTS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID ограничения ценообразования',
                required=True,
                type=int,
                location=OpenApiParameter.PATH,
            ),
        ],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_204_NO_CONTENT: None,
        },
    ),
)
class PricingConstraintViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, HasMainOfficeGroupPermission]
    authentication_classes = [JWTAuthentication]
    queryset = PricingConstraint.objects.all()
    serializer_class = PricingConstraintResponseSerializer
    lookup_field = 'id'


@extend_schema_view(
    create=extend_schema(
        summary='Создать запуск ценообразования',
        description='Создание нового запуска ценообразования',
        tags=[APISchemaTags.PRICING_RUNS],
        request=PricingRunRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_201_CREATED: PricingRunResponseSerializer,
        },
    ),
    list=extend_schema(
        summary='Получить список запусков ценообразования',
        description='Возвращает полный список всех запусков ценообразования',
        tags=[APISchemaTags.PRICING_RUNS],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: PricingRunResponseSerializer(many=True),
        },
    ),
    retrieve=extend_schema(
        summary='Получить запуск ценообразования по ID',
        description='Возвращает детальную информацию о конкретном запуске ценообразования',
        tags=[APISchemaTags.PRICING_RUNS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID запуска ценообразования',
                required=True,
                type=int,
                location=OpenApiParameter.PATH,
            ),
        ],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: PricingRunResponseSerializer,
        },
    ),
    update=extend_schema(
        summary='Обновить запуск ценообразования',
        description='Полное обновление информации о запуске ценообразования',
        tags=[APISchemaTags.PRICING_RUNS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID запуска ценообразования',
                required=True,
                type=int,
                location=OpenApiParameter.PATH,
            ),
        ],
        request=PricingRunRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: PricingRunResponseSerializer,
        },
    ),
    partial_update=extend_schema(
        summary='Частично обновить запуск ценообразования',
        description='Частичное обновление информации о запуске ценообразования',
        tags=[APISchemaTags.PRICING_RUNS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID запуска ценообразования',
                required=True,
                type=int,
                location=OpenApiParameter.PATH,
            ),
        ],
        request=PricingRunRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: PricingRunResponseSerializer,
        },
    ),
    destroy=extend_schema(
        summary='Удалить запуск ценообразования',
        description='Удаление запуска ценообразования из системы',
        tags=[APISchemaTags.PRICING_RUNS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID запуска ценообразования',
                required=True,
                type=int,
                location=OpenApiParameter.PATH,
            ),
        ],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_204_NO_CONTENT: None,
        },
    ),
)
class PricingRunViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, HasMainOfficeGroupPermission]
    authentication_classes = [JWTAuthentication]
    queryset = PricingRun.objects.all()
    serializer_class = PricingRunResponseSerializer
    lookup_field = 'id'


@extend_schema_view(
    create=extend_schema(
        summary='Создать цену магазина',
        description='Создание новой цены магазина',
        tags=[APISchemaTags.STORE_PRICES],
        request=StorePriceRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_201_CREATED: StorePriceResponseSerializer,
        },
    ),
    list=extend_schema(
        summary='Получить список цен магазинов',
        description='Возвращает полный список всех цен магазинов',
        tags=[APISchemaTags.STORE_PRICES],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: StorePriceResponseSerializer(many=True),
        },
    ),
    retrieve=extend_schema(
        summary='Получить цену магазина по ID',
        description='Возвращает детальную информацию о конкретной цене магазина',
        tags=[APISchemaTags.STORE_PRICES],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID цены магазина',
                required=True,
                type=int,
                location=OpenApiParameter.PATH,
            ),
        ],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: StorePriceResponseSerializer,
        },
    ),
    update=extend_schema(
        summary='Обновить цену магазина',
        description='Полное обновление информации о цене магазина',
        tags=[APISchemaTags.STORE_PRICES],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID цены магазина',
                required=True,
                type=int,
                location=OpenApiParameter.PATH,
            ),
        ],
        request=StorePriceRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: StorePriceResponseSerializer,
        },
    ),
    partial_update=extend_schema(
        summary='Частично обновить цену магазина',
        description='Частичное обновление информации о цене магазина',
        tags=[APISchemaTags.STORE_PRICES],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID цены магазина',
                required=True,
                type=int,
                location=OpenApiParameter.PATH,
            ),
        ],
        request=StorePriceRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: StorePriceResponseSerializer,
        },
    ),
    destroy=extend_schema(
        summary='Удалить цену магазина',
        description='Удаление цены магазина из системы',
        tags=[APISchemaTags.STORE_PRICES],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID цены магазина',
                required=True,
                type=int,
                location=OpenApiParameter.PATH,
            ),
        ],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_204_NO_CONTENT: None,
        },
    ),
)
class StorePriceViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, HasMainOfficeGroupPermission]
    authentication_classes = [JWTAuthentication]
    queryset = StorePrice.objects.all()
    serializer_class = StorePriceResponseSerializer
    lookup_field = 'id'


@extend_schema_view(
    create=extend_schema(
        summary='Создать купон',
        description='Создание нового купона',
        tags=[APISchemaTags.COUPONS],
        request=CouponRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_201_CREATED: CouponResponseSerializer,
        },
    ),
    list=extend_schema(
        summary='Получить список купонов',
        description='Возвращает полный список всех купонов',
        tags=[APISchemaTags.COUPONS],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: CouponResponseSerializer(many=True),
        },
    ),
    retrieve=extend_schema(
        summary='Получить купон по ID',
        description='Возвращает детальную информацию о конкретном купоне',
        tags=[APISchemaTags.COUPONS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID купона',
                required=True,
                type=int,
                location=OpenApiParameter.PATH,
            ),
        ],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: CouponResponseSerializer,
        },
    ),
    update=extend_schema(
        summary='Обновить купон',
        description='Полное обновление информации о купоне',
        tags=[APISchemaTags.COUPONS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID купона',
                required=True,
                type=int,
                location=OpenApiParameter.PATH,
            ),
        ],
        request=CouponRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: CouponResponseSerializer,
        },
    ),
    partial_update=extend_schema(
        summary='Частично обновить купон',
        description='Частичное обновление информации о купоне',
        tags=[APISchemaTags.COUPONS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID купона',
                required=True,
                type=int,
                location=OpenApiParameter.PATH,
            ),
        ],
        request=CouponRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: CouponResponseSerializer,
        },
    ),
    destroy=extend_schema(
        summary='Удалить купон',
        description='Удаление купона из системы',
        tags=[APISchemaTags.COUPONS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID купона',
                required=True,
                type=int,
                location=OpenApiParameter.PATH,
            ),
        ],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_204_NO_CONTENT: None,
        },
    ),
)
class CouponViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, HasMainOfficeGroupPermission]
    authentication_classes = [JWTAuthentication]
    queryset = Coupon.objects.all()
    serializer_class = CouponResponseSerializer
    lookup_field = 'id'


@extend_schema_view(
    create=extend_schema(
        summary='Создать чек продажи',
        description='Создание нового чека продажи',
        tags=[APISchemaTags.SALE_RECEIPTS],
        request=SaleReceiptRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_201_CREATED: SaleReceiptResponseSerializer,
        },
    ),
    list=extend_schema(
        summary='Получить список чеков продажи',
        description='Возвращает полный список всех чеков продажи',
        tags=[APISchemaTags.SALE_RECEIPTS],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: SaleReceiptResponseSerializer(many=True),
        },
    ),
    retrieve=extend_schema(
        summary='Получить чек продажи по ID',
        description='Возвращает детальную информацию о конкретном чеке продажи',
        tags=[APISchemaTags.SALE_RECEIPTS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID чека продажи',
                required=True,
                type=int,
                location=OpenApiParameter.PATH,
            ),
        ],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: SaleReceiptResponseSerializer,
        },
    ),
    update=extend_schema(
        summary='Обновить чек продажи',
        description='Полное обновление информации о чеке продажи',
        tags=[APISchemaTags.SALE_RECEIPTS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID чека продажи',
                required=True,
                type=int,
                location=OpenApiParameter.PATH,
            ),
        ],
        request=SaleReceiptRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: SaleReceiptResponseSerializer,
        },
    ),
    partial_update=extend_schema(
        summary='Частично обновить чек продажи',
        description='Частичное обновление информации о чеке продажи',
        tags=[APISchemaTags.SALE_RECEIPTS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID чека продажи',
                required=True,
                type=int,
                location=OpenApiParameter.PATH,
            ),
        ],
        request=SaleReceiptRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: SaleReceiptResponseSerializer,
        },
    ),
    destroy=extend_schema(
        summary='Удалить чек продажи',
        description='Удаление чека продажи из системы',
        tags=[APISchemaTags.SALE_RECEIPTS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID чека продажи',
                required=True,
                type=int,
                location=OpenApiParameter.PATH,
            ),
        ],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_204_NO_CONTENT: None,
        },
    ),
)
class SaleReceiptViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, HasSellerGroupPermission]
    authentication_classes = [JWTAuthentication]
    queryset = SaleReceipt.objects.all()
    serializer_class = SaleReceiptResponseSerializer
    lookup_field = 'id'


@extend_schema_view(
    create=extend_schema(
        summary='Создать строку чека',
        description='Создание новой строки чека',
        tags=[APISchemaTags.SALES_RECEIPT_LINES],
        request=SalesReceiptLineRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_201_CREATED: SalesReceiptLineResponseSerializer,
        },
    ),
    list=extend_schema(
        summary='Получить список строк чеков',
        description='Возвращает полный список всех строк чеков',
        tags=[APISchemaTags.SALES_RECEIPT_LINES],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: SalesReceiptLineResponseSerializer(many=True),
        },
    ),
    retrieve=extend_schema(
        summary='Получить строку чека по ID',
        description='Возвращает детальную информацию о конкретной строке чека',
        tags=[APISchemaTags.SALES_RECEIPT_LINES],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID строки чека',
                required=True,
                type=int,
                location=OpenApiParameter.PATH,
            ),
        ],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: SalesReceiptLineResponseSerializer,
        },
    ),
    update=extend_schema(
        summary='Обновить строку чека',
        description='Полное обновление информации о строке чека',
        tags=[APISchemaTags.SALES_RECEIPT_LINES],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID строки чека',
                required=True,
                type=int,
                location=OpenApiParameter.PATH,
            ),
        ],
        request=SalesReceiptLineRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: SalesReceiptLineResponseSerializer,
        },
    ),
    partial_update=extend_schema(
        summary='Частично обновить строку чека',
        description='Частичное обновление информации о строке чека',
        tags=[APISchemaTags.SALES_RECEIPT_LINES],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID строки чека',
                required=True,
                type=int,
                location=OpenApiParameter.PATH,
            ),
        ],
        request=SalesReceiptLineRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: SalesReceiptLineResponseSerializer,
        },
    ),
    destroy=extend_schema(
        summary='Удалить строку чека',
        description='Удаление строки чека из системы',
        tags=[APISchemaTags.SALES_RECEIPT_LINES],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID строки чека',
                required=True,
                type=int,
                location=OpenApiParameter.PATH,
            ),
        ],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_204_NO_CONTENT: None,
        },
    ),
)
class SalesReceiptLineViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, HasSellerGroupPermission]
    authentication_classes = [JWTAuthentication]
    queryset = SalesReceiptLine.objects.all()
    serializer_class = SalesReceiptLineResponseSerializer
    lookup_field = 'id'


@extend_schema_view(
    create=extend_schema(
        summary='Создать стоп-лист',
        description='Создание нового стоп-листа',
        tags=[APISchemaTags.STOP_LISTS],
        request=StopListRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_201_CREATED: StopListResponseSerializer,
        },
    ),
    list=extend_schema(
        summary='Получить список стоп-листов',
        description='Возвращает полный список всех стоп-листов',
        tags=[APISchemaTags.STOP_LISTS],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: StopListResponseSerializer(many=True),
        },
    ),
    retrieve=extend_schema(
        summary='Получить стоп-лист по ID',
        description='Возвращает детальную информацию о конкретном стоп-листе',
        tags=[APISchemaTags.STOP_LISTS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID стоп-листа',
                required=True,
                type=int,
                location=OpenApiParameter.PATH,
            ),
        ],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: StopListResponseSerializer,
        },
    ),
    update=extend_schema(
        summary='Обновить стоп-лист',
        description='Полное обновление информации о стоп-листе',
        tags=[APISchemaTags.STOP_LISTS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID стоп-листа',
                required=True,
                type=int,
                location=OpenApiParameter.PATH,
            ),
        ],
        request=StopListRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: StopListResponseSerializer,
        },
    ),
    partial_update=extend_schema(
        summary='Частично обновить стоп-лист',
        description='Частичное обновление информации о стоп-листе',
        tags=[APISchemaTags.STOP_LISTS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID стоп-листа',
                required=True,
                type=int,
                location=OpenApiParameter.PATH,
            ),
        ],
        request=StopListRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: StopListResponseSerializer,
        },
    ),
    destroy=extend_schema(
        summary='Удалить стоп-лист',
        description='Удаление стоп-листа из системы',
        tags=[APISchemaTags.STOP_LISTS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID стоп-листа',
                required=True,
                type=int,
                location=OpenApiParameter.PATH,
            ),
        ],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_204_NO_CONTENT: None,
        },
    ),
)
class StopListViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, HasMainOfficeGroupPermission]
    authentication_classes = [JWTAuthentication]
    queryset = StopList.objects.all()
    serializer_class = StopListResponseSerializer
    lookup_field = 'id'


@extend_schema_view(
    create=extend_schema(
        summary='Создать продукт в стоп-листе',
        description='Создание нового продукта в стоп-листе',
        tags=[APISchemaTags.STOP_LIST_PRODUCTS],
        request=StopListProductRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_201_CREATED: StopListProductResponseSerializer,
        },
    ),
    list=extend_schema(
        summary='Получить список продуктов в стоп-листах',
        description='Возвращает полный список всех продуктов в стоп-листах',
        tags=[APISchemaTags.STOP_LIST_PRODUCTS],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: StopListProductResponseSerializer(many=True),
        },
    ),
    retrieve=extend_schema(
        summary='Получить продукт в стоп-листе по ID',
        description='Возвращает детальную информацию о конкретном продукте в стоп-листе',
        tags=[APISchemaTags.STOP_LIST_PRODUCTS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID продукта в стоп-листе',
                required=True,
                type=int,
                location=OpenApiParameter.PATH,
            ),
        ],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: StopListProductResponseSerializer,
        },
    ),
    update=extend_schema(
        summary='Обновить продукт в стоп-листе',
        description='Полное обновление информации о продукте в стоп-листе',
        tags=[APISchemaTags.STOP_LIST_PRODUCTS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID продукта в стоп-листе',
                required=True,
                type=int,
                location=OpenApiParameter.PATH,
            ),
        ],
        request=StopListProductRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: StopListProductResponseSerializer,
        },
    ),
    partial_update=extend_schema(
        summary='Частично обновить продукт в стоп-листе',
        description='Частичное обновление информации о продукте в стоп-листе',
        tags=[APISchemaTags.STOP_LIST_PRODUCTS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID продукта в стоп-листе',
                required=True,
                type=int,
                location=OpenApiParameter.PATH,
            ),
        ],
        request=StopListProductRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: StopListProductResponseSerializer,
        },
    ),
    destroy=extend_schema(
        summary='Удалить продукт в стоп-листе',
        description='Удаление продукта в стоп-листе из системы',
        tags=[APISchemaTags.STOP_LIST_PRODUCTS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID продукта в стоп-листе',
                required=True,
                type=int,
                location=OpenApiParameter.PATH,
            ),
        ],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_204_NO_CONTENT: None,
        },
    ),
)
class StopListProductViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, HasMainOfficeGroupPermission]
    authentication_classes = [JWTAuthentication]
    queryset = StopListProduct.objects.all()
    serializer_class = StopListProductResponseSerializer
    lookup_field = 'id'


@extend_schema_view(
    create=extend_schema(
        summary='Создать инвентаризацию',
        description='Создание новой инвентаризации',
        tags=[APISchemaTags.STOCK_TAKES],
        request=StockTakeRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_201_CREATED: StockTakeResponseSerializer,
        },
    ),
    list=extend_schema(
        summary='Получить список инвентаризаций',
        description='Возвращает полный список всех инвентаризаций',
        tags=[APISchemaTags.STOCK_TAKES],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: StockTakeResponseSerializer(many=True),
        },
    ),
    retrieve=extend_schema(
        summary='Получить инвентаризацию по ID',
        description='Возвращает детальную информацию о конкретной инвентаризации',
        tags=[APISchemaTags.STOCK_TAKES],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID инвентаризации',
                required=True,
                type=int,
                location=OpenApiParameter.PATH,
            ),
        ],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: StockTakeResponseSerializer,
        },
    ),
    update=extend_schema(
        summary='Обновить инвентаризацию',
        description='Полное обновление информации об инвентаризации',
        tags=[APISchemaTags.STOCK_TAKES],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID инвентаризации',
                required=True,
                type=int,
                location=OpenApiParameter.PATH,
            ),
        ],
        request=StockTakeRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: StockTakeResponseSerializer,
        },
    ),
    partial_update=extend_schema(
        summary='Частично обновить инвентаризацию',
        description='Частичное обновление информации об инвентаризации',
        tags=[APISchemaTags.STOCK_TAKES],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID инвентаризации',
                required=True,
                type=int,
                location=OpenApiParameter.PATH,
            ),
        ],
        request=StockTakeRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: StockTakeResponseSerializer,
        },
    ),
    destroy=extend_schema(
        summary='Удалить инвентаризацию',
        description='Удаление инвентаризации из системы',
        tags=[APISchemaTags.STOCK_TAKES],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID инвентаризации',
                required=True,
                type=int,
                location=OpenApiParameter.PATH,
            ),
        ],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_204_NO_CONTENT: None,
        },
    ),
)
class StockTakeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, HasStorekeeperGroupPermission]
    authentication_classes = [JWTAuthentication]
    queryset = StockTake.objects.all()
    serializer_class = StockTakeResponseSerializer
    lookup_field = 'id'


@extend_schema_view(
    create=extend_schema(
        summary='Создать строку инвентаризации',
        description='Создание новой строки инвентаризации',
        tags=[APISchemaTags.STOCK_TAKE_LINES],
        request=StockTakeLineRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_201_CREATED: StockTakeLineResponseSerializer,
        },
    ),
    list=extend_schema(
        summary='Получить список строк инвентаризации',
        description='Возвращает полный список всех строк инвентаризации',
        tags=[APISchemaTags.STOCK_TAKE_LINES],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: StockTakeLineResponseSerializer(many=True),
        },
    ),
    retrieve=extend_schema(
        summary='Получить строку инвентаризации по ID',
        description='Возвращает детальную информацию о конкретной строке инвентаризации',
        tags=[APISchemaTags.STOCK_TAKE_LINES],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID строки инвентаризации',
                required=True,
                type=int,
                location=OpenApiParameter.PATH,
            ),
        ],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: StockTakeLineResponseSerializer,
        },
    ),
    update=extend_schema(
        summary='Обновить строку инвентаризации',
        description='Полное обновление информации о строке инвентаризации',
        tags=[APISchemaTags.STOCK_TAKE_LINES],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID строки инвентаризации',
                required=True,
                type=int,
                location=OpenApiParameter.PATH,
            ),
        ],
        request=StockTakeLineRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: StockTakeLineResponseSerializer,
        },
    ),
    partial_update=extend_schema(
        summary='Частично обновить строку инвентаризации',
        description='Частичное обновление информации о строке инвентаризации',
        tags=[APISchemaTags.STOCK_TAKE_LINES],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID строки инвентаризации',
                required=True,
                type=int,
                location=OpenApiParameter.PATH,
            ),
        ],
        request=StockTakeLineRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: StockTakeLineResponseSerializer,
        },
    ),
    destroy=extend_schema(
        summary='Удалить строку инвентаризации',
        description='Удаление строки инвентаризации из системы',
        tags=[APISchemaTags.STOCK_TAKE_LINES],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID строки инвентаризации',
                required=True,
                type=int,
                location=OpenApiParameter.PATH,
            ),
        ],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_204_NO_CONTENT: None,
        },
    ),
)
class StockTakeLineViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, HasStorekeeperGroupPermission]
    authentication_classes = [JWTAuthentication]
    queryset = StockTakeLine.objects.all()
    serializer_class = StockTakeLineResponseSerializer
    lookup_field = 'id'


@extend_schema_view(
    create=extend_schema(
        summary='Создать корректировку инвентаризации',
        description='Создание новой корректировки инвентаризации',
        tags=[APISchemaTags.STOCK_TAKE_ADJUSTMENTS],
        request=StockTakeAdjustmentRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_201_CREATED: StockTakeAdjustmentResponseSerializer,
        },
    ),
    list=extend_schema(
        summary='Получить список корректировок инвентаризации',
        description='Возвращает полный список всех корректировок инвентаризации',
        tags=[APISchemaTags.STOCK_TAKE_ADJUSTMENTS],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: StockTakeAdjustmentResponseSerializer(many=True),
        },
    ),
    retrieve=extend_schema(
        summary='Получить корректировку инвентаризации по ID',
        description='Возвращает детальную информацию о конкретной корректировке инвентаризации',
        tags=[APISchemaTags.STOCK_TAKE_ADJUSTMENTS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID корректировки инвентаризации',
                required=True,
                type=int,
                location=OpenApiParameter.PATH,
            ),
        ],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: StockTakeAdjustmentResponseSerializer,
        },
    ),
    update=extend_schema(
        summary='Обновить корректировку инвентаризации',
        description='Полное обновление информации о корректировке инвентаризации',
        tags=[APISchemaTags.STOCK_TAKE_ADJUSTMENTS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID корректировки инвентаризации',
                required=True,
                type=int,
                location=OpenApiParameter.PATH,
            ),
        ],
        request=StockTakeAdjustmentRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: StockTakeAdjustmentResponseSerializer,
        },
    ),
    partial_update=extend_schema(
        summary='Частично обновить корректировку инвентаризации',
        description='Частичное обновление информации о корректировке инвентаризации',
        tags=[APISchemaTags.STOCK_TAKE_ADJUSTMENTS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID корректировки инвентаризации',
                required=True,
                type=int,
                location=OpenApiParameter.PATH,
            ),
        ],
        request=StockTakeAdjustmentRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: StockTakeAdjustmentResponseSerializer,
        },
    ),
    destroy=extend_schema(
        summary='Удалить корректировку инвентаризации',
        description='Удаление корректировки инвентаризации из системы',
        tags=[APISchemaTags.STOCK_TAKE_ADJUSTMENTS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID корректировки инвентаризации',
                required=True,
                type=int,
                location=OpenApiParameter.PATH,
            ),
        ],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_204_NO_CONTENT: None,
        },
    ),
)
class StockTakeAdjustmentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, HasStorekeeperGroupPermission]
    authentication_classes = [JWTAuthentication]
    queryset = StockTakeAdjustment.objects.all()
    serializer_class = StockTakeAdjustmentResponseSerializer
    lookup_field = 'id'


@extend_schema_view(
    create=extend_schema(
        summary='Создать акт списания',
        description='Создание нового акта списания',
        tags=[APISchemaTags.WRITE_OFF_ACTS],
        request=WriteOffActRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_201_CREATED: WriteOffActResponseSerializer,
        },
    ),
    list=extend_schema(
        summary='Получить список актов списания',
        description='Возвращает полный список всех актов списания',
        tags=[APISchemaTags.WRITE_OFF_ACTS],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: WriteOffActResponseSerializer(many=True),
        },
    ),
    retrieve=extend_schema(
        summary='Получить акт списания по ID',
        description='Возвращает детальную информацию о конкретном акте списания',
        tags=[APISchemaTags.WRITE_OFF_ACTS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID акта списания',
                required=True,
                type=int,
                location=OpenApiParameter.PATH,
            ),
        ],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: WriteOffActResponseSerializer,
        },
    ),
    update=extend_schema(
        summary='Обновить акт списания',
        description='Полное обновление информации об акте списания',
        tags=[APISchemaTags.WRITE_OFF_ACTS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID акта списания',
                required=True,
                type=int,
                location=OpenApiParameter.PATH,
            ),
        ],
        request=WriteOffActRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: WriteOffActResponseSerializer,
        },
    ),
    partial_update=extend_schema(
        summary='Частично обновить акт списания',
        description='Частичное обновление информации об акте списания',
        tags=[APISchemaTags.WRITE_OFF_ACTS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID акта списания',
                required=True,
                type=int,
                location=OpenApiParameter.PATH,
            ),
        ],
        request=WriteOffActRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: WriteOffActResponseSerializer,
        },
    ),
    destroy=extend_schema(
        summary='Удалить акт списания',
        description='Удаление акта списания из системы',
        tags=[APISchemaTags.WRITE_OFF_ACTS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID акта списания',
                required=True,
                type=int,
                location=OpenApiParameter.PATH,
            ),
        ],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_204_NO_CONTENT: None,
        },
    ),
)
class WriteOffActViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, HasStorekeeperGroupPermission]
    authentication_classes = [JWTAuthentication]
    queryset = WriteOffAct.objects.all()
    serializer_class = WriteOffActResponseSerializer
    lookup_field = 'id'


@extend_schema_view(
    create=extend_schema(
        summary='Создать строку списания',
        description='Создание новой строки списания',
        tags=[APISchemaTags.WRITEOFF_LINES],
        request=WriteoffLineRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_201_CREATED: WriteoffLineResponseSerializer,
        },
    ),
    list=extend_schema(
        summary='Получить список строк списания',
        description='Возвращает полный список всех строк списания',
        tags=[APISchemaTags.WRITEOFF_LINES],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: WriteoffLineResponseSerializer(many=True),
        },
    ),
    retrieve=extend_schema(
        summary='Получить строку списания по ID',
        description='Возвращает детальную информацию о конкретной строке списания',
        tags=[APISchemaTags.WRITEOFF_LINES],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID строки списания',
                required=True,
                type=int,
                location=OpenApiParameter.PATH,
            ),
        ],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: WriteoffLineResponseSerializer,
        },
    ),
    update=extend_schema(
        summary='Обновить строку списания',
        description='Полное обновление информации о строке списания',
        tags=[APISchemaTags.WRITEOFF_LINES],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID строки списания',
                required=True,
                type=int,
                location=OpenApiParameter.PATH,
            ),
        ],
        request=WriteoffLineRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: WriteoffLineResponseSerializer,
        },
    ),
    partial_update=extend_schema(
        summary='Частично обновить строку списания',
        description='Частичное обновление информации о строке списания',
        tags=[APISchemaTags.WRITEOFF_LINES],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID строки списания',
                required=True,
                type=int,
                location=OpenApiParameter.PATH,
            ),
        ],
        request=WriteoffLineRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: WriteoffLineResponseSerializer,
        },
    ),
    destroy=extend_schema(
        summary='Удалить строку списания',
        description='Удаление строки списания из системы',
        tags=[APISchemaTags.WRITEOFF_LINES],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID строки списания',
                required=True,
                type=int,
                location=OpenApiParameter.PATH,
            ),
        ],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_204_NO_CONTENT: None,
        },
    ),
)
class WriteoffLineViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, HasStorekeeperGroupPermission]
    authentication_classes = [JWTAuthentication]
    queryset = WriteoffLine.objects.all()
    serializer_class = WriteoffLineResponseSerializer
    lookup_field = 'id'


@extend_schema_view(
    create=extend_schema(
        summary='Создать вложение списания',
        description='Создание нового вложения списания',
        tags=[APISchemaTags.WRITEOFF_ATTACHMENTS],
        request=WriteoffAttachmentRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_201_CREATED: WriteoffAttachmentResponseSerializer,
        },
    ),
    list=extend_schema(
        summary='Получить список вложений списания',
        description='Возвращает полный список всех вложений списания',
        tags=[APISchemaTags.WRITEOFF_ATTACHMENTS],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: WriteoffAttachmentResponseSerializer(many=True),
        },
    ),
    retrieve=extend_schema(
        summary='Получить вложение списания по ID',
        description='Возвращает детальную информацию о конкретном вложении списания',
        tags=[APISchemaTags.WRITEOFF_ATTACHMENTS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID вложения списания',
                required=True,
                type=int,
                location=OpenApiParameter.PATH,
            ),
        ],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: WriteoffAttachmentResponseSerializer,
        },
    ),
    update=extend_schema(
        summary='Обновить вложение списания',
        description='Полное обновление информации о вложении списания',
        tags=[APISchemaTags.WRITEOFF_ATTACHMENTS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID вложения списания',
                required=True,
                type=int,
                location=OpenApiParameter.PATH,
            ),
        ],
        request=WriteoffAttachmentRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: WriteoffAttachmentResponseSerializer,
        },
    ),
    partial_update=extend_schema(
        summary='Частично обновить вложение списания',
        description='Частичное обновление информации о вложении списания',
        tags=[APISchemaTags.WRITEOFF_ATTACHMENTS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID вложения списания',
                required=True,
                type=int,
                location=OpenApiParameter.PATH,
            ),
        ],
        request=WriteoffAttachmentRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: WriteoffAttachmentResponseSerializer,
        },
    ),
    destroy=extend_schema(
        summary='Удалить вложение списания',
        description='Удаление вложения списания из системы',
        tags=[APISchemaTags.WRITEOFF_ATTACHMENTS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID вложения списания',
                required=True,
                type=int,
                location=OpenApiParameter.PATH,
            ),
        ],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_204_NO_CONTENT: None,
        },
    ),
)
class WriteoffAttachmentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, HasStorekeeperGroupPermission]
    authentication_classes = [JWTAuthentication]
    queryset = WriteoffAttachment.objects.all()
    serializer_class = WriteoffAttachmentResponseSerializer
    lookup_field = 'id'


@extend_schema_view(
    create=extend_schema(
        summary='Создать проводку списания',
        description='Создание новой проводки списания',
        tags=[APISchemaTags.WRITEOFF_POSTINGS],
        request=WriteoffPostingRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_201_CREATED: WriteoffPostingResponseSerializer,
        },
    ),
    list=extend_schema(
        summary='Получить список проводок списания',
        description='Возвращает полный список всех проводок списания',
        tags=[APISchemaTags.WRITEOFF_POSTINGS],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: WriteoffPostingResponseSerializer(many=True),
        },
    ),
    retrieve=extend_schema(
        summary='Получить проводку списания по ID',
        description='Возвращает детальную информацию о конкретной проводке списания',
        tags=[APISchemaTags.WRITEOFF_POSTINGS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID проводки списания',
                required=True,
                type=int,
                location=OpenApiParameter.PATH,
            ),
        ],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: WriteoffPostingResponseSerializer,
        },
    ),
    update=extend_schema(
        summary='Обновить проводку списания',
        description='Полное обновление информации о проводке списания',
        tags=[APISchemaTags.WRITEOFF_POSTINGS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID проводки списания',
                required=True,
                type=int,
                location=OpenApiParameter.PATH,
            ),
        ],
        request=WriteoffPostingRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: WriteoffPostingResponseSerializer,
        },
    ),
    partial_update=extend_schema(
        summary='Частично обновить проводку списания',
        description='Частичное обновление информации о проводке списания',
        tags=[APISchemaTags.WRITEOFF_POSTINGS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID проводки списания',
                required=True,
                type=int,
                location=OpenApiParameter.PATH,
            ),
        ],
        request=WriteoffPostingRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: WriteoffPostingResponseSerializer,
        },
    ),
    destroy=extend_schema(
        summary='Удалить проводку списания',
        description='Удаление проводки списания из системы',
        tags=[APISchemaTags.WRITEOFF_POSTINGS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID проводки списания',
                required=True,
                type=int,
                location=OpenApiParameter.PATH,
            ),
        ],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_204_NO_CONTENT: None,
        },
    ),
)
class WriteoffPostingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, HasStorekeeperGroupPermission]
    authentication_classes = [JWTAuthentication]
    queryset = WriteoffPosting.objects.all()
    serializer_class = WriteoffPostingResponseSerializer
    lookup_field = 'id'


@extend_schema_view(
    create=extend_schema(
        summary="Создать партию товара",
        description='Создание новой партии товара',
        tags=[APISchemaTags.PRODUCT_INVENTORY_LOTS],
        request=ProductInventoryLotRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_201_CREATED: ProductInventoryLotResponseSerializer,
        },
    ),
    list=extend_schema(
        summary="Получить список партий товаров",
        description='Возвращает полный список всех партий товаров',
        tags=[APISchemaTags.PRODUCT_INVENTORY_LOTS],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: ProductInventoryLotRequestSerializer(many=True),
        },
    ),
    retrieve=extend_schema(
        summary="Получить партию товара по ID",
        description="Возвращает детальную информацию о конкретной партии товара",
        tags=[APISchemaTags.PRODUCT_INVENTORY_LOTS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID партии товара',
                required=True,
                type=int,
                location=OpenApiParameter.PATH
            ),
        ],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: ProductInventoryLotResponseSerializer,
        },
    ),
    update=extend_schema(
        summary="Обновить партию товара",
        description='Полное обновление информации о партии товара',
        tags=[APISchemaTags.PRODUCT_INVENTORY_LOTS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID партии товара',
                required=True,
                type=int,
                location=OpenApiParameter.PATH
            ),
        ],
        request=ProductInventoryLotRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: ProductInventoryLotResponseSerializer,
        },
    ),
    partial_update=extend_schema(
        summary="Частично обновить партию товара",
        description='Частичное обновление информации о партии товара',
        tags=[APISchemaTags.PRODUCT_INVENTORY_LOTS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID партии товара',
                required=True,
                type=int,
                location=OpenApiParameter.PATH
            ),
        ],
        request=ProductInventoryLotRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: ProductInventoryLotResponseSerializer,
        },
    ),
    destroy=extend_schema(
        summary="Удалить партию товара",
        description='Удаление партии товара из системы',
        tags=[APISchemaTags.PRODUCT_INVENTORY_LOTS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID партии товара',
                required=True,
                type=int,
                location=OpenApiParameter.PATH
            ),
        ],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_204_NO_CONTENT: None,
        },
    ),
)
class ProductInventoryLotViewSet(viewsets.ModelViewSet):
    """CRUD операции для партий товаров"""

    permission_classes = [IsAuthenticated, HasStorekeeperGroupPermission]
    authentication_classes = [JWTAuthentication]
    queryset = ProductInventoryLot.objects.all()
    serializer_class = ProductInventoryLotResponseSerializer
    lookup_field = 'id'
