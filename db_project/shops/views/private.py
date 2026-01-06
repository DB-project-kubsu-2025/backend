from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from common_utils.constants import APISchemaTags, DefaultAPIResponses
from common_utils.permissions import HasStorekeeperGroupPermission
from shops.models import Space
from shops.serializers import SpaceRequestSerializer


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
