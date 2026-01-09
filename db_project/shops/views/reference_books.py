from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from common_utils.constants import APISchemaTags, DefaultAPIResponses
from common_utils.permissions import HasMainOfficeGroupPermission
from shops.models import (
    ProductUnit,
    ProductCategory,
    WriteoffReason,
    StockTakeType,
    StopListReason,
    PaymentMethod,
    CouponDiscountType,
    PriceListBase,
    PriceListType,
    MovementType,
    SpaceType,
    StorageType,
    Product,
    StorageProfile,
)
from shops.serializers import (
    ProductUnitRequestSerializer,
    ProductCategoryRequestSerializer,
    WriteoffReasonRequestSerializer,
    StockTakeTypeRequestSerializer,
    StopListReasonRequestSerializer,
    PaymentMethodRequestSerializer,
    CouponDiscountTypeRequestSerializer,
    PriceListBaseRequestSerializer,
    PriceListTypeRequestSerializer,
    MovementTypeRequestSerializer,
    SpaceTypeRequestSerializer,
    StorageTypeRequestSerializer,
    ProductRequestSerializer,
    StorageProfileRequestSerializer,
    PaymentMethodResponseSerializer,
    StopListReasonResponseSerializer,
    StockTakeTypeResponseSerializer,
    WriteoffReasonResponseSerializer,
    CouponDiscountTypeResponseSerializer,
    PriceListBaseResponseSerializer,
    PriceListTypeResponseSerializer,
    MovementTypeResponseSerializer,
    SpaceTypeResponseSerializer,
    StorageTypeResponseSerializer,
    StorageProfileResponseSerializer,
    ProductResponseSerializer,
    ProductCategoryResponseSerializer,
    ProductUnitResponseSerializer,
)


@extend_schema_view(
    create=extend_schema(
        summary="Создать единицу измерения",
        description='Создание новой единицы измерения товаров в справочнике',
        tags=[APISchemaTags.PRODUCTS],
        request=ProductUnitRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_201_CREATED: ProductUnitResponseSerializer,
        },
    ),
    list=extend_schema(
        summary="Получить список единиц измерения",
        description='Возвращает полный список всех единиц измерения товаров из справочника',
        tags=[APISchemaTags.PRODUCTS],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: ProductUnitResponseSerializer(many=True),
        },
    ),
    retrieve=extend_schema(
        summary="Получить единицу измерения по ID",
        description="Возвращает детальную информацию о конкретной единице измерения товара",
        tags=[APISchemaTags.PRODUCTS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID единицы измерения',
                required=True,
                type=int,
                location=OpenApiParameter.PATH
            ),
        ],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: ProductUnitResponseSerializer,
        },
    ),
    update=extend_schema(
        summary="Обновить единицу измерения",
        description='Полное обновление информации о единице измерения',
        tags=[APISchemaTags.PRODUCTS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID единицы измерения',
                required=True,
                type=int,
                location=OpenApiParameter.PATH
            ),
        ],
        request=ProductUnitRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: ProductUnitResponseSerializer,
        },
    ),
    partial_update=extend_schema(
        summary="Частично обновить единицу измерения",
        description='Частичное обновление информации о единице измерения',
        tags=[APISchemaTags.PRODUCTS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID единицы измерения',
                required=True,
                type=int,
                location=OpenApiParameter.PATH
            ),
        ],
        request=ProductUnitRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: ProductUnitResponseSerializer,
        },
    ),
    destroy=extend_schema(
        summary="Удалить единицу измерения",
        description='Удаление единицы измерения из справочника',
        tags=[APISchemaTags.PRODUCTS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID единицы измерения',
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
class ProductUnitViewSet(ModelViewSet):
    """CRUD операции для справочника единиц измерения"""

    permission_classes = [IsAuthenticated, HasMainOfficeGroupPermission]
    authentication_classes = [JWTAuthentication]
    queryset = ProductUnit.objects.all()
    serializer_class = ProductUnitRequestSerializer
    lookup_field = 'id'


@extend_schema_view(
    create=extend_schema(
        summary="Создать категорию продукта",
        description='Создание новой категории товаров в справочнике',
        tags=[APISchemaTags.CATEGORIES],
        request=ProductCategoryRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_201_CREATED: ProductCategoryResponseSerializer,
        },
    ),
    list=extend_schema(
        summary="Получить список категорий продуктов",
        description='Возвращает полный список всех категорий товаров из справочника',
        tags=[APISchemaTags.CATEGORIES],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: ProductCategoryResponseSerializer(many=True),
        },
    ),
    retrieve=extend_schema(
        summary="Получить категорию товара по ID",
        description="Возвращает детальную информацию о конкретной категории товара",
        tags=[APISchemaTags.CATEGORIES],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID категории',
                required=True,
                type=int,
                location=OpenApiParameter.PATH
            ),
        ],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: ProductCategoryResponseSerializer,
        },
    ),
    update=extend_schema(
        summary="Обновить категорию продукта",
        description='Полное обновление информации о категории продукта',
        tags=[APISchemaTags.CATEGORIES],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID категории',
                required=True,
                type=int,
                location=OpenApiParameter.PATH
            ),
        ],
        request=ProductCategoryRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: ProductCategoryResponseSerializer,
        },
    ),
    partial_update=extend_schema(
        summary="Частично обновить категорию продукта",
        description='Частичное обновление информации о категории продукта',
        tags=[APISchemaTags.CATEGORIES],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID категории',
                required=True,
                type=int,
                location=OpenApiParameter.PATH
            ),
        ],
        request=ProductCategoryRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: ProductCategoryResponseSerializer,
        },
    ),
    destroy=extend_schema(
        summary="Удалить категорию продукта",
        description='Удаление категории продукта из справочника',
        tags=[APISchemaTags.CATEGORIES],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID категории',
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
class ProductCategoryViewSet(ModelViewSet):
    """CRUD операции для справочника категорий продуктов"""

    permission_classes = [IsAuthenticated, HasMainOfficeGroupPermission]
    authentication_classes = [JWTAuthentication]
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategoryRequestSerializer
    lookup_field = 'id'


@extend_schema_view(
    create=extend_schema(
        summary="Создать продукт",
        description='Создание нового продукта в справочнике',
        tags=[APISchemaTags.PRODUCTS],
        request=ProductRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_201_CREATED: ProductResponseSerializer,
        },
    ),
    list=extend_schema(
        summary="Получить список продуктов",
        description='Возвращает полный список всех продуктов из справочника',
        tags=[APISchemaTags.PRODUCTS],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: ProductResponseSerializer(many=True),
        },
    ),
    retrieve=extend_schema(
        summary="Получить продукт по ID",
        description="Возвращает детальную информацию о конкретном продукте",
        tags=[APISchemaTags.PRODUCTS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID продукта',
                required=True,
                type=int,
                location=OpenApiParameter.PATH
            ),
        ],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: ProductResponseSerializer,
        },
    ),
    update=extend_schema(
        summary="Обновить продукт",
        description='Полное обновление информации о продукте',
        tags=[APISchemaTags.PRODUCTS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID продукта',
                required=True,
                type=int,
                location=OpenApiParameter.PATH,
            ),
        ],
        request=ProductRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: ProductResponseSerializer,
        },
    ),
    partial_update=extend_schema(
        summary="Частично обновить продукт",
        description='Частичное обновление информации о продукте',
        tags=[APISchemaTags.PRODUCTS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID продукта',
                required=True,
                type=int,
                location=OpenApiParameter.PATH,
            ),
        ],
        request=ProductRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: ProductResponseSerializer,
        },
    ),
    destroy=extend_schema(
        summary="Удалить продукт",
        description='Удаление продукта из справочника',
        tags=[APISchemaTags.PRODUCTS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID продукта',
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
class ProductViewSet(ModelViewSet):
    """CRUD операции для справочника продуктов"""

    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    queryset = Product.objects.all()
    serializer_class = ProductRequestSerializer
    lookup_field = 'id'


@extend_schema_view(
    create=extend_schema(
        summary="Создать условие хранения",
        description='Создание нового условия хранения продукта',
        tags=[APISchemaTags.PRODUCTS],
        request=StorageProfileRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_201_CREATED: StorageProfileResponseSerializer,
        },
    ),
    list=extend_schema(
        summary="Получить список условий хранения",
        description='Возвращает полный список всех условий хранения продуктов',
        tags=[APISchemaTags.PRODUCTS],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: StorageProfileResponseSerializer(many=True),
        },
    ),
    retrieve=extend_schema(
        summary="Получить условие хранения по ID",
        description="Возвращает детальную информацию о конкретном условии хранения продукта",
        tags=[APISchemaTags.PRODUCTS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID условия хранения',
                required=True,
                type=int,
                location=OpenApiParameter.PATH
            ),
        ],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: StorageProfileResponseSerializer,
        },
    ),
    update=extend_schema(
        summary="Обновить условие хранения",
        description='Полное обновление информации об условии хранения',
        tags=[APISchemaTags.PRODUCTS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID условия хранения',
                required=True,
                type=int,
                location=OpenApiParameter.PATH
            ),
        ],
        request=StorageProfileRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: StorageProfileResponseSerializer,
        },
    ),
    partial_update=extend_schema(
        summary="Частично обновить условие хранения",
        description='Частичное обновление информации об условии хранения',
        tags=[APISchemaTags.PRODUCTS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID условия хранения',
                required=True,
                type=int,
                location=OpenApiParameter.PATH
            ),
        ],
        request=StorageProfileRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: StorageProfileResponseSerializer,
        },
    ),
    destroy=extend_schema(
        summary="Удалить условие хранения",
        description='Удаление условия хранения из системы',
        tags=[APISchemaTags.PRODUCTS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID условия хранения',
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
class StorageProfileViewSet(ModelViewSet):
    """CRUD операции для справочника условий хранения продуктов"""

    permission_classes = [IsAuthenticated, HasMainOfficeGroupPermission]
    authentication_classes = [JWTAuthentication]
    queryset = StorageProfile.objects.all()
    serializer_class = StorageProfileRequestSerializer
    lookup_field = 'id'


@extend_schema_view(
    create=extend_schema(
        summary="Создать тип хранилища",
        description='Создание нового типа хранилища в справочнике',
        tags=[APISchemaTags.STORAGES],
        request=StorageTypeRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_201_CREATED: StorageTypeResponseSerializer,
        },
    ),
    list=extend_schema(
        summary="Получить список типов хранилищ",
        description='Возвращает полный список всех типов хранилищ из справочника',
        tags=[APISchemaTags.STORAGES],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: StorageTypeResponseSerializer(many=True),
        },
    ),
    retrieve=extend_schema(
        summary="Получить тип хранилища по ID",
        description="Возвращает детальную информацию о конкретном типе хранилища",
        tags=[APISchemaTags.STORAGES],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID типа хранилища',
                required=True,
                type=int,
                location=OpenApiParameter.PATH
            ),
        ],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: StorageTypeResponseSerializer,
        },
    ),
    update=extend_schema(
        summary="Обновить тип хранилища",
        description='Полное обновление информации о типе хранилища',
        tags=[APISchemaTags.STORAGES],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID типа хранилища',
                required=True,
                type=int,
                location=OpenApiParameter.PATH
            ),
        ],
        request=StorageTypeRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: StorageTypeResponseSerializer,
        },
    ),
    partial_update=extend_schema(
        summary="Частично обновить тип хранилища",
        description='Частичное обновление информации о типе хранилища',
        tags=[APISchemaTags.STORAGES],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID типа хранилища',
                required=True,
                type=int,
                location=OpenApiParameter.PATH
            ),
        ],
        request=StorageTypeRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: StorageTypeResponseSerializer,
        },
    ),
    destroy=extend_schema(
        summary="Удалить тип хранилища",
        description='Удаление типа хранилища из справочника',
        tags=[APISchemaTags.STORAGES],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID типа хранилища',
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
class StorageTypeViewSet(ModelViewSet):
    """CRUD операции для справочника типов хранилищ"""

    permission_classes = [IsAuthenticated, HasMainOfficeGroupPermission]
    authentication_classes = [JWTAuthentication]
    queryset = StorageType.objects.all()
    serializer_class = StorageTypeRequestSerializer
    lookup_field = 'id'


@extend_schema_view(
    create=extend_schema(
        summary="Создать тип места хранения",
        description='Создание нового типа места хранения в справочнике',
        tags=[APISchemaTags.SPACES],
        request=SpaceTypeRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_201_CREATED: SpaceTypeResponseSerializer,
        },
    ),
    list=extend_schema(
        summary="Получить список типов мест хранения",
        description='Возвращает полный список всех типов мест хранения из справочника',
        tags=[APISchemaTags.SPACES],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: SpaceTypeResponseSerializer(many=True),
        },
    ),
    retrieve=extend_schema(
        summary="Получить тип места хранения по ID",
        description="Возвращает детальную информацию о конкретном типе места хранения",
        tags=[APISchemaTags.SPACES],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID типа места хранения',
                required=True,
                type=int,
                location=OpenApiParameter.PATH
            ),
        ],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: SpaceTypeResponseSerializer,
        },
    ),
    update=extend_schema(
        summary="Обновить тип места хранения",
        description='Полное обновление информации о типе места хранения',
        tags=[APISchemaTags.SPACES],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID типа места хранения',
                required=True,
                type=int,
                location=OpenApiParameter.PATH
            ),
        ],
        request=SpaceTypeRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: SpaceTypeResponseSerializer,
        },
    ),
    partial_update=extend_schema(
        summary="Частично обновить тип места хранения",
        description='Частичное обновление информации о типе места хранения',
        tags=[APISchemaTags.SPACES],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID типа места хранения',
                required=True,
                type=int,
                location=OpenApiParameter.PATH
            ),
        ],
        request=SpaceTypeRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: SpaceTypeResponseSerializer,
        },
    ),
    destroy=extend_schema(
        summary="Удалить тип места хранения",
        description='Удаление типа места хранения из справочника',
        tags=[APISchemaTags.SPACES],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID типа места хранения',
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
class SpaceTypeViewSet(ModelViewSet):
    """CRUD операции для справочника типов мест хранения"""

    permission_classes = [IsAuthenticated, HasMainOfficeGroupPermission]
    authentication_classes = [JWTAuthentication]
    queryset = SpaceType.objects.all()
    serializer_class = SpaceTypeRequestSerializer
    lookup_field = 'id'


@extend_schema_view(
    create=extend_schema(
        summary="Создать тип перемещения",
        description='Создание нового типа перемещения в справочнике',
        tags=[APISchemaTags.MOVEMENT_TYPES],
        request=MovementTypeRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_201_CREATED: MovementTypeResponseSerializer,
        },
    ),
    list=extend_schema(
        summary="Получить список типов перемещений",
        description='Возвращает полный список всех типов перемещений партий из справочника',
        tags=[APISchemaTags.MOVEMENT_TYPES],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: MovementTypeResponseSerializer(many=True),
        },
    ),
    retrieve=extend_schema(
        summary="Получить тип перемещения по ID",
        description="Возвращает детальную информацию о конкретном типе перемещения партии",
        tags=[APISchemaTags.MOVEMENT_TYPES],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID типа перемещения',
                required=True,
                type=int,
                location=OpenApiParameter.PATH
            ),
        ],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: MovementTypeResponseSerializer,
        },
    ),
    update=extend_schema(
        summary="Обновить тип перемещения",
        description='Полное обновление информации о типе перемещения',
        tags=[APISchemaTags.MOVEMENT_TYPES],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID типа перемещения',
                required=True,
                type=int,
                location=OpenApiParameter.PATH
            ),
        ],
        request=MovementTypeRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: MovementTypeResponseSerializer,
        },
    ),
    partial_update=extend_schema(
        summary="Частично обновить тип перемещения",
        description='Частичное обновление информации о типе перемещения',
        tags=[APISchemaTags.MOVEMENT_TYPES],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID типа перемещения',
                required=True,
                type=int,
                location=OpenApiParameter.PATH
            ),
        ],
        request=MovementTypeRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: MovementTypeResponseSerializer,
        },
    ),
    destroy=extend_schema(
        summary="Удалить тип перемещения",
        description='Удаление типа перемещения из справочника',
        tags=[APISchemaTags.MOVEMENT_TYPES],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID типа перемещения',
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
class MovementTypeViewSet(ModelViewSet):
    """CRUD операции для справочника типов перемещений"""

    permission_classes = [IsAuthenticated, HasMainOfficeGroupPermission]
    authentication_classes = [JWTAuthentication]
    queryset = MovementType.objects.all()
    serializer_class = MovementTypeRequestSerializer
    lookup_field = 'id'


@extend_schema_view(
    create=extend_schema(
        summary="Создать тип прайс-листа",
        description='Создание нового типа прайс-листа в справочнике',
        tags=[APISchemaTags.PRICE_LISTS],
        request=PriceListTypeRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_201_CREATED: PriceListTypeResponseSerializer,
        },
    ),
    list=extend_schema(
        summary="Получить список типов прайс-листов",
        description='Возвращает полный список всех типов прайс-листов из справочника',
        tags=[APISchemaTags.PRICE_LISTS],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: PriceListTypeResponseSerializer(many=True),
        },
    ),
    retrieve=extend_schema(
        summary="Получить тип прайс-листа по ID",
        description="Возвращает детальную информацию о конкретном типе прайс-листа",
        tags=[APISchemaTags.PRICE_LISTS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID типа прайс-листа',
                required=True,
                type=int,
                location=OpenApiParameter.PATH
            ),
        ],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: PriceListTypeResponseSerializer,
        },
    ),
    update=extend_schema(
        summary="Обновить тип прайс-листа",
        description='Полное обновление информации о типе прайс-листа',
        tags=[APISchemaTags.PRICE_LISTS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID типа прайс-листа',
                required=True,
                type=int,
                location=OpenApiParameter.PATH
            ),
        ],
        request=PriceListTypeRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: PriceListTypeResponseSerializer,
        },
    ),
    partial_update=extend_schema(
        summary="Частично обновить тип прайс-листа",
        description='Частичное обновление информации о типе прайс-листа',
        tags=[APISchemaTags.PRICE_LISTS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID типа прайс-листа',
                required=True,
                type=int,
                location=OpenApiParameter.PATH
            ),
        ],
        request=PriceListTypeRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: PriceListTypeResponseSerializer,
        },
    ),
    destroy=extend_schema(
        summary="Удалить тип прайс-листа",
        description='Удаление типа прайс-листа из справочника',
        tags=[APISchemaTags.PRICE_LISTS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID типа прайс-листа',
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
class PriceListTypeViewSet(ModelViewSet):
    """CRUD операции для справочника типов прайс-листов"""

    permission_classes = [IsAuthenticated, HasMainOfficeGroupPermission]
    authentication_classes = [JWTAuthentication]
    queryset = PriceListType.objects.all()
    serializer_class = PriceListTypeRequestSerializer
    lookup_field = 'id'


@extend_schema_view(
    create=extend_schema(
        summary="Создать основание прайс-листа",
        description='Создание нового основания формирования прайс-листа в справочнике',
        tags=[APISchemaTags.PRICE_LISTS],
        request=PriceListBaseRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_201_CREATED: PriceListBaseResponseSerializer,
        },
    ),
    list=extend_schema(
        summary="Получить список оснований прайс-листов",
        description='Возвращает полный список всех оснований формирования прайс-листов из справочника',
        tags=[APISchemaTags.PRICE_LISTS],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: PriceListBaseResponseSerializer(many=True),
        },
    ),
    retrieve=extend_schema(
        summary="Получить основание прайс-листа по ID",
        description="Возвращает детальную информацию о конкретном основании формирования прайс-листа",
        tags=[APISchemaTags.PRICE_LISTS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID основания прайс-листа',
                required=True,
                type=int,
                location=OpenApiParameter.PATH
            ),
        ],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: PriceListBaseResponseSerializer,
        },
    ),
    update=extend_schema(
        summary="Обновить основание прайс-листа",
        description='Полное обновление информации об основании прайс-листа',
        tags=[APISchemaTags.PRICE_LISTS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID основания прайс-листа',
                required=True,
                type=int,
                location=OpenApiParameter.PATH
            ),
        ],
        request=PriceListBaseRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: PriceListBaseResponseSerializer,
        },
    ),
    partial_update=extend_schema(
        summary="Частично обновить основание прайс-листа",
        description='Частичное обновление информации об основании прайс-листа',
        tags=[APISchemaTags.PRICE_LISTS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID основания прайс-листа',
                required=True,
                type=int,
                location=OpenApiParameter.PATH
            ),
        ],
        request=PriceListBaseRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: PriceListBaseResponseSerializer,
        },
    ),
    destroy=extend_schema(
        summary="Удалить основание прайс-листа",
        description='Удаление основания прайс-листа из справочника',
        tags=[APISchemaTags.PRICE_LISTS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID основания прайс-листа',
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
class PriceListBaseViewSet(ModelViewSet):
    """CRUD операции для справочника оснований прайс-листов"""

    permission_classes = [IsAuthenticated, HasMainOfficeGroupPermission]
    authentication_classes = [JWTAuthentication]
    queryset = PriceListBase.objects.all()
    serializer_class = PriceListBaseRequestSerializer
    lookup_field = 'id'


@extend_schema_view(
    create=extend_schema(
        summary="Создать тип скидки в купоне",
        description='Создание нового типа скидки в купоне в справочнике',
        tags=[APISchemaTags.DISCOUNT_TYPES],
        request=CouponDiscountTypeRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_201_CREATED: CouponDiscountTypeResponseSerializer,
        },
    ),
    list=extend_schema(
        summary="Получить список типов скидок в купонах",
        description='Возвращает полный список всех типов скидок в купонах из справочника',
        tags=[APISchemaTags.DISCOUNT_TYPES],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: CouponDiscountTypeResponseSerializer(many=True),
        },
    ),
    retrieve=extend_schema(
        summary="Получить тип скидки в купоне по ID",
        description="Возвращает детальную информацию о конкретном типе скидки в купоне",
        tags=[APISchemaTags.DISCOUNT_TYPES],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID типа скидки',
                required=True,
                type=int,
                location=OpenApiParameter.PATH
            ),
        ],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: CouponDiscountTypeResponseSerializer,
        },
    ),
    update=extend_schema(
        summary="Обновить тип скидки в купоне",
        description='Полное обновление информации о типе скидки в купоне',
        tags=[APISchemaTags.DISCOUNT_TYPES],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID типа скидки',
                required=True,
                type=int,
                location=OpenApiParameter.PATH
            ),
        ],
        request=CouponDiscountTypeRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: CouponDiscountTypeResponseSerializer,
        },
    ),
    partial_update=extend_schema(
        summary="Частично обновить тип скидки в купоне",
        description='Частичное обновление информации о типе скидки в купоне',
        tags=[APISchemaTags.DISCOUNT_TYPES],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID типа скидки',
                required=True,
                type=int,
                location=OpenApiParameter.PATH
            ),
        ],
        request=CouponDiscountTypeRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: CouponDiscountTypeResponseSerializer,
        },
    ),
    destroy=extend_schema(
        summary="Удалить тип скидки в купоне",
        description='Удаление типа скидки в купоне из справочника',
        tags=[APISchemaTags.DISCOUNT_TYPES],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID типа скидки',
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
class CouponDiscountTypeViewSet(ModelViewSet):
    """CRUD операции для справочника типов скидок в купонах"""

    permission_classes = [IsAuthenticated, HasMainOfficeGroupPermission]
    authentication_classes = [JWTAuthentication]
    queryset = CouponDiscountType.objects.all()
    serializer_class = CouponDiscountTypeRequestSerializer
    lookup_field = 'id'


@extend_schema_view(
    create=extend_schema(
        summary="Создать тип оплаты",
        description='Создание нового типа оплаты в справочнике',
        tags=[APISchemaTags.PAYMENT_TYPES],
        request=PaymentMethodRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_201_CREATED: PaymentMethodResponseSerializer,
        },
    ),
    list=extend_schema(
        summary="Получить список типов оплаты",
        description='Возвращает полный список всех типов оплаты из справочника',
        tags=[APISchemaTags.PAYMENT_TYPES],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: PaymentMethodResponseSerializer(many=True),
        },
    ),
    retrieve=extend_schema(
        summary="Получить тип оплаты по ID",
        description="Возвращает детальную информацию о конкретном типе оплаты",
        tags=[APISchemaTags.PAYMENT_TYPES],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID типа оплаты',
                required=True,
                type=int,
                location=OpenApiParameter.PATH
            ),
        ],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: PaymentMethodResponseSerializer,
        },
    ),
    update=extend_schema(
        summary="Обновить тип оплаты",
        description='Полное обновление информации о типе оплаты',
        tags=[APISchemaTags.PAYMENT_TYPES],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID типа оплаты',
                required=True,
                type=int,
                location=OpenApiParameter.PATH
            ),
        ],
        request=PaymentMethodRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: PaymentMethodResponseSerializer,
        },
    ),
    partial_update=extend_schema(
        summary="Частично обновить тип оплаты",
        description='Частичное обновление информации о типе оплаты',
        tags=[APISchemaTags.PAYMENT_TYPES],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID типа оплаты',
                required=True,
                type=int,
                location=OpenApiParameter.PATH
            ),
        ],
        request=PaymentMethodRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: PaymentMethodResponseSerializer,
        },
    ),
    destroy=extend_schema(
        summary="Удалить тип оплаты",
        description='Удаление типа оплаты из справочника',
        tags=[APISchemaTags.PAYMENT_TYPES],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID типа оплаты',
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
class PaymentMethodViewSet(ModelViewSet):
    """CRUD операции для справочника типов оплаты"""

    permission_classes = [IsAuthenticated, HasMainOfficeGroupPermission]
    authentication_classes = [JWTAuthentication]
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodRequestSerializer
    lookup_field = 'id'


@extend_schema_view(
    create=extend_schema(
        summary="Создать причину стоп-листа",
        description='Создание новой причины переноса в стоп-лист в справочнике',
        tags=[APISchemaTags.STOP_LISTS],
        request=StopListReasonRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_201_CREATED: StopListReasonResponseSerializer,
        },
    ),
    list=extend_schema(
        summary="Получить список причин стоп-листа",
        description='Возвращает полный список всех причин переноса в стоп-лист из справочника',
        tags=[APISchemaTags.STOP_LISTS],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: StopListReasonResponseSerializer(many=True),
        },
    ),
    retrieve=extend_schema(
        summary="Получить причину стоп-листа по ID",
        description="Возвращает детальную информацию о конкретной причине переноса в стоп-лист",
        tags=[APISchemaTags.STOP_LISTS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID причины стоп-листа',
                required=True,
                type=int,
                location=OpenApiParameter.PATH
            ),
        ],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: StopListReasonResponseSerializer,
        },
    ),
    update=extend_schema(
        summary="Обновить причину стоп-листа",
        description='Полное обновление информации о причине стоп-листа',
        tags=[APISchemaTags.STOP_LISTS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID причины стоп-листа',
                required=True,
                type=int,
                location=OpenApiParameter.PATH
            ),
        ],
        request=StopListReasonRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: StopListReasonResponseSerializer,
        },
    ),
    partial_update=extend_schema(
        summary="Частично обновить причину стоп-листа",
        description='Частичное обновление информации о причине стоп-листа',
        tags=[APISchemaTags.STOP_LISTS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID причины стоп-листа',
                required=True,
                type=int,
                location=OpenApiParameter.PATH
            ),
        ],
        request=StopListReasonRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: StopListReasonResponseSerializer,
        },
    ),
    destroy=extend_schema(
        summary="Удалить причину стоп-листа",
        description='Удаление причины стоп-листа из справочника',
        tags=[APISchemaTags.STOP_LISTS],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID причины стоп-листа',
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
class StopListReasonViewSet(ModelViewSet):
    """CRUD операции для справочника причин стоп-листа"""

    permission_classes = [IsAuthenticated, HasMainOfficeGroupPermission]
    authentication_classes = [JWTAuthentication]
    queryset = StopListReason.objects.all()
    serializer_class = StopListReasonRequestSerializer
    lookup_field = 'id'


@extend_schema_view(
    create=extend_schema(
        summary="Создать тип инвентаризации",
        description='Создание нового типа инвентаризации в справочнике',
        tags=[APISchemaTags.INVENTORY],
        request=StockTakeTypeRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_201_CREATED: StockTakeTypeResponseSerializer,
        },
    ),
    list=extend_schema(
        summary="Получить список типов инвентаризации",
        description='Возвращает полный список всех типов инвентаризации из справочника',
        tags=[APISchemaTags.INVENTORY],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: StockTakeTypeResponseSerializer(many=True),
        },
    ),
    retrieve=extend_schema(
        summary="Получить тип инвентаризации по ID",
        description="Возвращает детальную информацию о конкретном типе инвентаризации",
        tags=[APISchemaTags.INVENTORY],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID типа инвентаризации',
                required=True,
                type=int,
                location=OpenApiParameter.PATH
            ),
        ],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: StockTakeTypeResponseSerializer,
        },
    ),
    update=extend_schema(
        summary="Обновить тип инвентаризации",
        description='Полное обновление информации о типе инвентаризации',
        tags=[APISchemaTags.INVENTORY],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID типа инвентаризации',
                required=True,
                type=int,
                location=OpenApiParameter.PATH
            ),
        ],
        request=StockTakeTypeRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: StockTakeTypeResponseSerializer,
        },
    ),
    partial_update=extend_schema(
        summary="Частично обновить тип инвентаризации",
        description='Частичное обновление информации о типе инвентаризации',
        tags=[APISchemaTags.INVENTORY],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID типа инвентаризации',
                required=True,
                type=int,
                location=OpenApiParameter.PATH
            ),
        ],
        request=StockTakeTypeRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: StockTakeTypeResponseSerializer,
        },
    ),
    destroy=extend_schema(
        summary="Удалить тип инвентаризации",
        description='Удаление типа инвентаризации из справочника',
        tags=[APISchemaTags.INVENTORY],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID типа инвентаризации',
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
class StockTakeTypeViewSet(ModelViewSet):
    """CRUD операции для справочника типов инвентаризации"""

    permission_classes = [IsAuthenticated, HasMainOfficeGroupPermission]
    authentication_classes = [JWTAuthentication]
    queryset = StockTakeType.objects.all()
    serializer_class = StockTakeTypeRequestSerializer
    lookup_field = 'id'


@extend_schema_view(
    create=extend_schema(
        summary="Создать причину списания",
        description='Создание новой причины списания в справочнике',
        tags=[APISchemaTags.WRITEOFF],
        request=WriteoffReasonRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_201_CREATED: WriteoffReasonResponseSerializer,
        },
    ),
    list=extend_schema(
        summary="Получить список причин списания",
        description='Возвращает полный список всех причин списания из справочника',
        tags=[APISchemaTags.WRITEOFF],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: WriteoffReasonResponseSerializer(many=True),
        },
    ),
    retrieve=extend_schema(
        summary="Получить причину списания по ID",
        description="Возвращает детальную информацию о конкретной причине списания",
        tags=[APISchemaTags.WRITEOFF],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID причины списания',
                required=True,
                type=int,
                location=OpenApiParameter.PATH
            ),
        ],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: WriteoffReasonResponseSerializer,
        },
    ),
    update=extend_schema(
        summary="Обновить причину списания",
        description='Полное обновление информации о причине списания',
        tags=[APISchemaTags.WRITEOFF],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID причины списания',
                required=True,
                type=int,
                location=OpenApiParameter.PATH
            ),
        ],
        request=WriteoffReasonRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: WriteoffReasonResponseSerializer,
        },
    ),
    partial_update=extend_schema(
        summary="Частично обновить причину списания",
        description='Частичное обновление информации о причине списания',
        tags=[APISchemaTags.WRITEOFF],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID причины списания',
                required=True,
                type=int,
                location=OpenApiParameter.PATH
            ),
        ],
        request=WriteoffReasonRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: WriteoffReasonResponseSerializer,
        },
    ),
    destroy=extend_schema(
        summary="Удалить причину списания",
        description='Удаление причины списания из справочника',
        tags=[APISchemaTags.WRITEOFF],
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID причины списания',
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
class WriteoffReasonViewSet(ModelViewSet):
    """CRUD операции для справочника причин списания"""

    permission_classes = [IsAuthenticated, HasMainOfficeGroupPermission]
    authentication_classes = [JWTAuthentication]
    queryset = WriteoffReason.objects.all()
    serializer_class = WriteoffReasonRequestSerializer
    lookup_field = 'id'
