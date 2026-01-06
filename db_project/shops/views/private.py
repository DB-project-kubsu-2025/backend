from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from common_utils.constants import APISchemaTags, DefaultAPIResponses
from common_utils.permissions import (
    HasStorekeeperGroupPermission,
    HasCommodityExpertGroupPermission,
    HasMainOfficeGroupPermission,
)
from shops.models import Space, InventoryLot, Storage
from shops.serializers import SpaceRequestSerializer, InventoryLotRequestSerializer, StorageRequestSerializer


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
                location=OpenApiParameter.PATH
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
    serializer_class = StorageRequestSerializer
    lookup_field = 'id'


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
    serializer_class = SpaceRequestSerializer
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
        tags=[APISchemaTags.INVENTORY],
        request=InventoryLotRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_201_CREATED: InventoryLotRequestSerializer,
        },
    ),
    list=extend_schema(
        summary="Получить список партий товара",
        description='Возвращает полный список всех партий товаров',
        tags=[APISchemaTags.INVENTORY],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: InventoryLotRequestSerializer(many=True),
        },
    ),
    retrieve=extend_schema(
        summary="Получить партию товара по ID",
        description="Возвращает детальную информацию о конкретной партии товара",
        tags=[APISchemaTags.INVENTORY],
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
        tags=[APISchemaTags.INVENTORY],
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
        tags=[APISchemaTags.INVENTORY],
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
        tags=[APISchemaTags.INVENTORY],
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
    serializer_class = InventoryLotRequestSerializer
    lookup_field = 'id'
