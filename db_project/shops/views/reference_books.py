from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from common_utils.constants import APISchemaTags, DefaultAPIResponses
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
    StorageType, Product,
)
from shops.serializers import (
    ProductUnitResponseSerializer,
    ProductCategoryResponseSerializer,
    WriteoffReasonResponseSerializer,
    StockTakeTypeResponseSerializer,
    StopListReasonResponseSerializer,
    PaymentMethodResponseSerializer,
    CouponDiscountTypeResponseSerializer,
    PriceListBaseResponseSerializer,
    PriceListTypeResponseSerializer,
    MovementTypeResponseSerializer,
    SpaceTypeResponseSerializer,
    StorageTypeResponseSerializer, ProductResponseSerializer,
)


@extend_schema_view(
    list=extend_schema(
        summary="Получить список единиц измерения",
        description='Возвращает полный список всех единиц измерения товаров из справочника',
        tags=[APISchemaTags.REFERENCE_BOOKS, APISchemaTags.SHOPS],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: ProductUnitResponseSerializer(many=True),
        },
    ),
    retrieve=extend_schema(
        summary="Получить единицу измерения по ID",
        description="Возвращает детальную информацию о конкретной единице измерения товара",
        tags=["Справочники"],
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
)
class GetProductUnit(ReadOnlyModelViewSet):
    """Получить данные из справочника единиц измерения"""

    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    queryset = ProductUnit.objects.all()
    serializer_class = ProductUnitResponseSerializer
    lookup_field = 'id'


@extend_schema_view(
    list=extend_schema(
        summary="Получить список категорий продуктов",
        description='Возвращает полный список всех категорий товаров из справочника',
        tags=[APISchemaTags.REFERENCE_BOOKS, APISchemaTags.SHOPS],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: ProductUnitResponseSerializer(many=True),
        },
    ),
    retrieve=extend_schema(
        summary="Получить категорию товара по ID",
        description="Возвращает детальную информацию о конкретной категории товара",
        tags=["Справочники"],
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
            status.HTTP_200_OK: ProductCategoryResponseSerializer,
        },
    ),
)
class GetProductCategory(ReadOnlyModelViewSet):
    """Получить данные из справочника категорий продуктов"""

    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategoryResponseSerializer
    lookup_field = 'id'


@extend_schema_view(
    list=extend_schema(
        summary="Получить список продуктов",
        description='Возвращает полный список всех продуктов из справочника',
        tags=[APISchemaTags.REFERENCE_BOOKS, APISchemaTags.SHOPS],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: ProductResponseSerializer(many=True),
        },
    ),
    retrieve=extend_schema(
        summary="Получить продукт по ID",
        description="Возвращает детальную информацию о конкретном продукте",
        tags=[APISchemaTags.REFERENCE_BOOKS, APISchemaTags.SHOPS],
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
)
class GetProduct(ReadOnlyModelViewSet):
    """Получить данные из справочника продуктов"""

    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    queryset = Product.objects.all()
    serializer_class = ProductResponseSerializer
    lookup_field = 'id'


@extend_schema_view(
    list=extend_schema(
        summary="Получить список типов хранилищ",
        description='Возвращает полный список всех типов хранилищ из справочника',
        tags=[APISchemaTags.REFERENCE_BOOKS],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: StorageTypeResponseSerializer(many=True),
        },
    ),
    retrieve=extend_schema(
        summary="Получить тип хранилища по ID",
        description="Возвращает детальную информацию о конкретном типе хранилища",
        tags=[APISchemaTags.REFERENCE_BOOKS],
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
)
class GetStorageType(ReadOnlyModelViewSet):
    """Получить данные из справочника типов хранилищ"""

    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    queryset = StorageType.objects.all()
    serializer_class = StorageTypeResponseSerializer
    lookup_field = 'id'


@extend_schema_view(
    list=extend_schema(
        summary="Получить список типов мест хранения",
        description='Возвращает полный список всех типов мест хранения из справочника',
        tags=[APISchemaTags.REFERENCE_BOOKS],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: SpaceTypeResponseSerializer(many=True),
        },
    ),
    retrieve=extend_schema(
        summary="Получить тип места хранения по ID",
        description="Возвращает детальную информацию о конкретном типе места хранения",
        tags=[APISchemaTags.REFERENCE_BOOKS],
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
)
class GetSpaceType(ReadOnlyModelViewSet):
    """Получить данные из справочника типов мест хранения"""

    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    queryset = SpaceType.objects.all()
    serializer_class = SpaceTypeResponseSerializer
    lookup_field = 'id'


@extend_schema_view(
    list=extend_schema(
        summary="Получить список типов перемещений",
        description='Возвращает полный список всех типов перемещений партий из справочника',
        tags=[APISchemaTags.REFERENCE_BOOKS],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: MovementTypeResponseSerializer(many=True),
        },
    ),
    retrieve=extend_schema(
        summary="Получить тип перемещения по ID",
        description="Возвращает детальную информацию о конкретном типе перемещения партии",
        tags=[APISchemaTags.REFERENCE_BOOKS],
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
)
class GetMovementType(ReadOnlyModelViewSet):
    """Получить данные из справочника типов перемещений"""

    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    queryset = MovementType.objects.all()
    serializer_class = MovementTypeResponseSerializer
    lookup_field = 'id'


@extend_schema_view(
    list=extend_schema(
        summary="Получить список типов прайс-листов",
        description='Возвращает полный список всех типов прайс-листов из справочника',
        tags=[APISchemaTags.REFERENCE_BOOKS],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: PriceListTypeResponseSerializer(many=True),
        },
    ),
    retrieve=extend_schema(
        summary="Получить тип прайс-листа по ID",
        description="Возвращает детальную информацию о конкретном типе прайс-листа",
        tags=[APISchemaTags.REFERENCE_BOOKS],
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
)
class GetPriceListType(ReadOnlyModelViewSet):
    """Получить данные из справочника типов прайс-листов"""

    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    queryset = PriceListType.objects.all()
    serializer_class = PriceListTypeResponseSerializer
    lookup_field = 'id'


@extend_schema_view(
    list=extend_schema(
        summary="Получить список оснований прайс-листов",
        description='Возвращает полный список всех оснований формирования прайс-листов из справочника',
        tags=[APISchemaTags.REFERENCE_BOOKS],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: PriceListBaseResponseSerializer(many=True),
        },
    ),
    retrieve=extend_schema(
        summary="Получить основание прайс-листа по ID",
        description="Возвращает детальную информацию о конкретном основании формирования прайс-листа",
        tags=[APISchemaTags.REFERENCE_BOOKS],
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
)
class GetPriceListBase(ReadOnlyModelViewSet):
    """Получить данные из справочника оснований прайс-листов"""

    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    queryset = PriceListBase.objects.filter(is_active=True)
    serializer_class = PriceListBaseResponseSerializer
    lookup_field = 'id'


@extend_schema_view(
    list=extend_schema(
        summary="Получить список типов скидок в купонах",
        description='Возвращает полный список всех типов скидок в купонах из справочника',
        tags=[APISchemaTags.REFERENCE_BOOKS],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: CouponDiscountTypeResponseSerializer(many=True),
        },
    ),
    retrieve=extend_schema(
        summary="Получить тип скидки в купоне по ID",
        description="Возвращает детальную информацию о конкретном типе скидки в купоне",
        tags=[APISchemaTags.REFERENCE_BOOKS],
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
)
class GetCouponDiscountType(ReadOnlyModelViewSet):
    """Получить данные из справочника типов скидок в купонах"""

    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    queryset = CouponDiscountType.objects.all()
    serializer_class = CouponDiscountTypeResponseSerializer
    lookup_field = 'id'


@extend_schema_view(
    list=extend_schema(
        summary="Получить список типов оплаты",
        description='Возвращает полный список всех типов оплаты из справочника',
        tags=[APISchemaTags.REFERENCE_BOOKS],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: PaymentMethodResponseSerializer(many=True),
        },
    ),
    retrieve=extend_schema(
        summary="Получить тип оплаты по ID",
        description="Возвращает детальную информацию о конкретном типе оплаты",
        tags=[APISchemaTags.REFERENCE_BOOKS],
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
)
class GetPaymentMethod(ReadOnlyModelViewSet):
    """Получить данные из справочника типов оплаты"""

    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodResponseSerializer
    lookup_field = 'id'


@extend_schema_view(
    list=extend_schema(
        summary="Получить список причин стоп-листа",
        description='Возвращает полный список всех причин переноса в стоп-лист из справочника',
        tags=[APISchemaTags.REFERENCE_BOOKS],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: StopListReasonResponseSerializer(many=True),
        },
    ),
    retrieve=extend_schema(
        summary="Получить причину стоп-листа по ID",
        description="Возвращает детальную информацию о конкретной причине переноса в стоп-лист",
        tags=[APISchemaTags.REFERENCE_BOOKS],
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
)
class GetStopListReason(ReadOnlyModelViewSet):
    """Получить данные из справочника причин стоп-листа"""

    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    queryset = StopListReason.objects.all()
    serializer_class = StopListReasonResponseSerializer
    lookup_field = 'id'


@extend_schema_view(
    list=extend_schema(
        summary="Получить список типов инвентаризации",
        description='Возвращает полный список всех типов инвентаризации из справочника',
        tags=[APISchemaTags.REFERENCE_BOOKS],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: StockTakeTypeResponseSerializer(many=True),
        },
    ),
    retrieve=extend_schema(
        summary="Получить тип инвентаризации по ID",
        description="Возвращает детальную информацию о конкретном типе инвентаризации",
        tags=[APISchemaTags.REFERENCE_BOOKS],
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
)
class GetStockTakeType(ReadOnlyModelViewSet):
    """Получить данные из справочника типов инвентаризации"""

    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    queryset = StockTakeType.objects.filter(is_active=True)
    serializer_class = StockTakeTypeResponseSerializer
    lookup_field = 'id'


@extend_schema_view(
    list=extend_schema(
        summary="Получить список причин списания",
        description='Возвращает полный список всех причин списания из справочника',
        tags=[APISchemaTags.REFERENCE_BOOKS],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: WriteoffReasonResponseSerializer(many=True),
        },
    ),
    retrieve=extend_schema(
        summary="Получить причину списания по ID",
        description="Возвращает детальную информацию о конкретной причине списания",
        tags=[APISchemaTags.REFERENCE_BOOKS],
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
)
class GetWriteoffReason(ReadOnlyModelViewSet):
    """Получить данные из справочника причин списания"""

    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    queryset = WriteoffReason.objects.filter(is_active=True)
    serializer_class = WriteoffReasonResponseSerializer
    lookup_field = 'id'
