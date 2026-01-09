from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from common_utils.constants import APISchemaTags, DefaultAPIResponses
from employees.models import (
    JobPosition,
    WorkingRate,
    Workplace,
    Employee,
    LeaveRequestType,
    TimeSessionCloseReason,
)
from employees.serializers.response_serializers import (
    JobPositionResponseSerializer,
    WorkingRateResponseSerializer,
    WorkplaceResponseSerializer,
    EmployeeResponseSerializer,
    LeaveRequestTypeResponseSerializer,
    TimeSessionCloseReasonResponseSerializer,
)


@extend_schema_view(
    list=extend_schema(
        summary="Получить список должностей",
        description="Возвращает полный список справочника должностей",
        tags=[APISchemaTags.EMPLOYEES],
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_200_OK: JobPositionResponseSerializer(many=True)},
    ),
    retrieve=extend_schema(
        summary="Получить должность по ID",
        description="Детальная информация по должности",
        tags=[APISchemaTags.EMPLOYEES],
        parameters=[
            OpenApiParameter(name="id", description="ID должности", required=True, type=int, location=OpenApiParameter.PATH)
        ],
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_200_OK: JobPositionResponseSerializer},
    ),
)
class GetJobPosition(ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    queryset = JobPosition.objects.all()
    serializer_class = JobPositionResponseSerializer
    lookup_field = "id"


@extend_schema_view(
    list=extend_schema(
        summary="Получить список рабочих ставок",
        description="Возвращает полный список справочника рабочих ставок",
        tags=[APISchemaTags.EMPLOYEES],
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_200_OK: WorkingRateResponseSerializer(many=True)},
    ),
    retrieve=extend_schema(
        summary="Получить рабочую ставку по ID",
        description="Детальная информация по рабочей ставке",
        tags=[APISchemaTags.EMPLOYEES],
        parameters=[
            OpenApiParameter(name="id", description="ID ставки", required=True, type=int, location=OpenApiParameter.PATH)
        ],
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_200_OK: WorkingRateResponseSerializer},
    ),
)
class GetWorkingRate(ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    queryset = WorkingRate.objects.all()
    serializer_class = WorkingRateResponseSerializer
    lookup_field = "id"


@extend_schema_view(
    list=extend_schema(
        summary="Получить список рабочих мест",
        description="Возвращает полный список справочника рабочих мест",
        tags=[APISchemaTags.EMPLOYEES],
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_200_OK: WorkplaceResponseSerializer(many=True)},
    ),
    retrieve=extend_schema(
        summary="Получить рабочее место по ID",
        description="Детальная информация по рабочему месту",
        tags=[APISchemaTags.EMPLOYEES],
        parameters=[OpenApiParameter(name="id", description="ID рабочего места", required=True, type=int, location=OpenApiParameter.PATH)],
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_200_OK: WorkplaceResponseSerializer},
    ),
)
class GetWorkplace(ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    queryset = Workplace.objects.all()
    serializer_class = WorkplaceResponseSerializer
    lookup_field = "id"


@extend_schema_view(
    list=extend_schema(
        summary="Получить список сотрудников",
        description="Возвращает список сотрудников (справочник работников). Поля включают паспорт, рабочее место и группы.",
        tags=[APISchemaTags.EMPLOYEES],
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_200_OK: EmployeeResponseSerializer(many=True)},
    ),
    retrieve=extend_schema(
        summary="Получить сотрудника по ID",
        description="Детальная информация по сотруднику, включая паспорт и рабочее место",
        tags=[APISchemaTags.EMPLOYEES],
        parameters=[OpenApiParameter(name="id", description="ID сотрудника", required=True, type=int, location=OpenApiParameter.PATH)],
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_200_OK: EmployeeResponseSerializer},
    ),
)
class GetEmployee(ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    queryset = Employee.objects.select_related("passport", "workplace__storage", "workplace__main_office_filial").all()
    serializer_class = EmployeeResponseSerializer
    lookup_field = "id"


@extend_schema_view(
    list=extend_schema(
        summary="Получить список типов запросов на отсутствие",
        description="Справочник типов временных отсутствий (отпуск, больничный и т.д.)",
        tags=[APISchemaTags.EMPLOYEES],
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_200_OK: LeaveRequestTypeResponseSerializer(many=True)},
    ),
    retrieve=extend_schema(
        summary="Получить тип запроса на отсутствие по ID",
        description="Детальная информация по типу запроса на отсутствие",
        tags=[APISchemaTags.EMPLOYEES],
        parameters=[OpenApiParameter(name="id", description="ID типа", required=True, type=int, location=OpenApiParameter.PATH)],
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_200_OK: LeaveRequestTypeResponseSerializer},
    ),
)
class GetLeaveRequestType(ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    queryset = LeaveRequestType.objects.all()
    serializer_class = LeaveRequestTypeResponseSerializer
    lookup_field = "id"


@extend_schema_view(
    list=extend_schema(
        summary="Получить список причин закрытия сессии",
        description="Справочник причин закрытия рабочих сессий",
        tags=[APISchemaTags.EMPLOYEES],
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_200_OK: TimeSessionCloseReasonResponseSerializer(many=True)},
    ),
    retrieve=extend_schema(
        summary="Получить причину закрытия сессии по ID",
        description="Детальная информация по причине закрытия сессии",
        tags=[APISchemaTags.EMPLOYEES],
        parameters=[OpenApiParameter(name="id", description="ID причины", required=True, type=int, location=OpenApiParameter.PATH)],
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_200_OK: TimeSessionCloseReasonResponseSerializer},
    ),
)
class GetTimeSessionCloseReason(ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    queryset = TimeSessionCloseReason.objects.all()
    serializer_class = TimeSessionCloseReasonResponseSerializer
    lookup_field = "id"