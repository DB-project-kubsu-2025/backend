from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter, OpenApiResponse, OpenApiExample
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from common_utils.constants import APISchemaTags, DefaultAPIResponses
from common_utils.permissions import HasMainOfficeGroupPermission

from employees.models import (
    Passport,
    WorkingRate,
    JobPosition,
    Salary,
    Workplace,
    Employee,
    LeaveRequestType,
    LeaveRequest,
    LeaveRequestAttachment,
    AnnualLeaveBalance,
    TimeEntry,
    TimeSessionCloseReason,
    TimeSession,
    TimeDay,
)
from employees.selectors import get_user_groups
from employees.serializers.request_serializers import (
    PassportRequestSerializer,
    WorkingRateRequestSerializer,
    JobPositionRequestSerializer,
    SalaryRequestSerializer,
    WorkplaceRequestSerializer,
    EmployeeRequestSerializer,
    LeaveRequestTypeRequestSerializer,
    LeaveRequestRequestSerializer,
    LeaveRequestAttachmentRequestSerializer,
    AnnualLeaveBalanceRequestSerializer,
    TimeEntryRequestSerializer,
    TimeSessionCloseReasonRequestSerializer,
    TimeSessionRequestSerializer,
    TimeDayRequestSerializer,
)
from employees.serializers.response_serializers import (
    PassportResponseSerializer,
    WorkingRateResponseSerializer,
    JobPositionResponseSerializer,
    SalaryResponseSerializer,
    WorkplaceResponseSerializer,
    EmployeeResponseSerializer,
    LeaveRequestTypeResponseSerializer,
    LeaveRequestResponseSerializer,
    LeaveRequestAttachmentResponseSerializer,
    AnnualLeaveBalanceResponseSerializer,
    TimeEntryResponseSerializer,
    TimeSessionCloseReasonResponseSerializer,
    TimeSessionResponseSerializer,
    TimeDayResponseSerializer,
)



@extend_schema_view(
    create=extend_schema(
        summary="Создать паспорт",
        description="Создание записи паспорта",
        tags=[APISchemaTags.EMPLOYEES],
        request=PassportRequestSerializer,
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_201_CREATED: PassportRequestSerializer},
    ),
    list=extend_schema(
        summary="Получить список паспортов",
        description="Возвращает полный список паспортов сотрудников",
        tags=[APISchemaTags.EMPLOYEES],
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_200_OK: PassportRequestSerializer(many=True)},
    ),
    retrieve=extend_schema(
        summary="Получить паспорт по ID",
        description="Детальная информация по паспорту",
        tags=[APISchemaTags.EMPLOYEES],
        parameters=[OpenApiParameter(name="id", description="ID паспорта", required=True, type=int, location=OpenApiParameter.PATH)],
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_200_OK: PassportRequestSerializer},
    ),
    update=extend_schema(
        summary="Обновить паспорт",
        description="Полное обновление паспорта",
        tags=[APISchemaTags.EMPLOYEES],
        request=PassportRequestSerializer,
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_200_OK: PassportRequestSerializer},
    ),
    partial_update=extend_schema(
        summary="Частично обновить паспорт",
        description="Частичное обновление паспорта",
        tags=[APISchemaTags.EMPLOYEES],
        request=PassportRequestSerializer,
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_200_OK: PassportRequestSerializer},
    ),
    destroy=extend_schema(
        summary="Удалить паспорт",
        description="Удаление паспорта из системы",
        tags=[APISchemaTags.EMPLOYEES],
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_204_NO_CONTENT: None},
    ),
)
class PassportViewSet(viewsets.ModelViewSet):
    """CRUD операции для паспортов сотрудников"""
    authentication_classes = [JWTAuthentication]
    queryset = Passport.objects.all()
    serializer_class = PassportRequestSerializer
    lookup_field = "id"

    def get_permissions(self):
        # read: authenticated; write: main office (admin)
        if self.action in ["list", "retrieve"]:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated, HasMainOfficeGroupPermission]
        return [p() for p in permission_classes]


@extend_schema_view(
    create=extend_schema(
        summary="Создать должность",
        description="Создание новой должности",
        tags=[APISchemaTags.EMPLOYEES],
        request=JobPositionRequestSerializer,
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_201_CREATED: JobPositionRequestSerializer},
    ),
    list=extend_schema(
        summary="Получить список должностей",
        description="Возвращает справочник должностей",
        tags=[APISchemaTags.EMPLOYEES],
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_200_OK: JobPositionRequestSerializer(many=True)},
    ),
    retrieve=extend_schema(
        summary="Получить должность по ID",
        description="Детальная информация по должности",
        tags=[APISchemaTags.EMPLOYEES],
        parameters=[OpenApiParameter(name="id", description="ID должности", required=True, type=int, location=OpenApiParameter.PATH)],
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_200_OK: JobPositionRequestSerializer},
    ),
    update=extend_schema(
        summary="Обновить должность",
        description="Полное обновление должности",
        tags=[APISchemaTags.EMPLOYEES],
        request=JobPositionRequestSerializer,
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_200_OK: JobPositionRequestSerializer},
    ),
    partial_update=extend_schema(
        summary="Частично обновить должность",
        description="Частичное обновление должности",
        tags=[APISchemaTags.EMPLOYEES],
        request=JobPositionRequestSerializer,
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_200_OK: JobPositionRequestSerializer},
    ),
    destroy=extend_schema(
        summary="Удалить должность",
        description="Удаление должности из справочника",
        tags=[APISchemaTags.EMPLOYEES],
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_204_NO_CONTENT: None},
    ),
)
class JobPositionViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    queryset = JobPosition.objects.all()
    serializer_class = JobPositionRequestSerializer
    lookup_field = "id"

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated, HasMainOfficeGroupPermission]
        return [p() for p in permission_classes]


@extend_schema_view(
    create=extend_schema(
        summary="Создать рабочую ставку",
        description="Создание новой рабочей ставки",
        tags=[APISchemaTags.EMPLOYEES],
        request=WorkingRateRequestSerializer,
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_201_CREATED: WorkingRateRequestSerializer},
    ),
    list=extend_schema(
        summary="Получить список рабочих ставок",
        description="Справочник рабочих ставок",
        tags=[APISchemaTags.EMPLOYEES],
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_200_OK: WorkingRateRequestSerializer(many=True)},
    ),
    retrieve=extend_schema(
        summary="Получить рабочую ставку по ID",
        description="Детальная информация по рабочей ставке",
        tags=[APISchemaTags.EMPLOYEES],
        parameters=[OpenApiParameter(name="id", description="ID ставки", required=True, type=int, location=OpenApiParameter.PATH)],
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_200_OK: WorkingRateRequestSerializer},
    ),
    update=extend_schema(
        summary="Обновить рабочую ставку",
        description="Полное обновление рабочей ставки",
        tags=[APISchemaTags.EMPLOYEES],
        request=WorkingRateRequestSerializer,
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_200_OK: WorkingRateRequestSerializer},
    ),
    partial_update=extend_schema(
        summary="Частично обновить рабочую ставку",
        description="Частичное обновление рабочей ставки",
        tags=[APISchemaTags.EMPLOYEES],
        request=WorkingRateRequestSerializer,
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_200_OK: WorkingRateRequestSerializer},
    ),
    destroy=extend_schema(
        summary="Удалить рабочую ставку",
        description="Удаление рабочей ставки",
        tags=[APISchemaTags.EMPLOYEES],
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_204_NO_CONTENT: None},
    ),
)
class WorkingRateViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    queryset = WorkingRate.objects.all()
    serializer_class = WorkingRateRequestSerializer
    lookup_field = "id"

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated, HasMainOfficeGroupPermission]
        return [p() for p in permission_classes]


@extend_schema_view(
    create=extend_schema(
        summary="Создать зарплату",
        description="Создание записи зарплаты для должности",
        tags=[APISchemaTags.EMPLOYEES],
        request=SalaryRequestSerializer,
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_201_CREATED: SalaryRequestSerializer},
    ),
    list=extend_schema(
        summary="Получить список зарплат",
        description="Справочник зарплат по должностям",
        tags=[APISchemaTags.EMPLOYEES],
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_200_OK: SalaryRequestSerializer(many=True)},
    ),
    retrieve=extend_schema(
        summary="Получить зарплату по ID",
        description="Детальная информация по записи зарплаты",
        tags=[APISchemaTags.EMPLOYEES],
        parameters=[OpenApiParameter(name="id", description="ID записи", required=True, type=int, location=OpenApiParameter.PATH)],
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_200_OK: SalaryRequestSerializer},
    ),
    update=extend_schema(
        summary="Обновить запись зарплаты",
        description="Полное обновление записи зарплаты",
        tags=[APISchemaTags.EMPLOYEES],
        request=SalaryRequestSerializer,
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_200_OK: SalaryRequestSerializer},
    ),
    partial_update=extend_schema(
        summary="Частично обновить запись зарплаты",
        description="Частичное обновление записи зарплаты",
        tags=[APISchemaTags.EMPLOYEES],
        request=SalaryRequestSerializer,
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_200_OK: SalaryRequestSerializer},
    ),
    destroy=extend_schema(
        summary="Удалить запись зарплаты",
        description="Удаление записи зарплаты",
        tags=[APISchemaTags.EMPLOYEES],
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_204_NO_CONTENT: None},
    ),
)
class SalaryViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    queryset = Salary.objects.select_related("job_position", "working_rate").all()
    serializer_class = SalaryRequestSerializer
    lookup_field = "id"

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated, HasMainOfficeGroupPermission]
        return [p() for p in permission_classes]


@extend_schema_view(
    create=extend_schema(
        summary="Создать рабочее место",
        description="Создание рабочего места (связь с хранилищем или филиалом)",
        tags=[APISchemaTags.EMPLOYEES],
        request=WorkplaceRequestSerializer,
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_201_CREATED: WorkplaceRequestSerializer},
    ),
    list=extend_schema(
        summary="Получить список рабочих мест",
        description="Справочник рабочих мест",
        tags=[APISchemaTags.EMPLOYEES],
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_200_OK: WorkplaceRequestSerializer(many=True)},
    ),
    retrieve=extend_schema(
        summary="Получить рабочее место по ID",
        description="Детальная информация по рабочему месту",
        tags=[APISchemaTags.EMPLOYEES],
        parameters=[OpenApiParameter(name="id", description="ID рабочего места", required=True, type=int, location=OpenApiParameter.PATH)],
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_200_OK: WorkplaceRequestSerializer},
    ),
    update=extend_schema(
        summary="Обновить рабочее место",
        description="Полное обновление рабочего места",
        tags=[APISchemaTags.EMPLOYEES],
        request=WorkplaceRequestSerializer,
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_200_OK: WorkplaceRequestSerializer},
    ),
    partial_update=extend_schema(
        summary="Частично обновить рабочее место",
        description="Частичное обновление рабочего места",
        tags=[APISchemaTags.EMPLOYEES],
        request=WorkplaceRequestSerializer,
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_200_OK: WorkplaceRequestSerializer},
    ),
    destroy=extend_schema(
        summary="Удалить рабочее место",
        description="Удаление рабочего места",
        tags=[APISchemaTags.EMPLOYEES],
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_204_NO_CONTENT: None},
    ),
)
class WorkplaceViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    queryset = Workplace.objects.select_related("storage", "main_office_filial").all()
    serializer_class = WorkplaceRequestSerializer
    lookup_field = "id"

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated, HasMainOfficeGroupPermission]
        return [p() for p in permission_classes]


@extend_schema_view(
    create=extend_schema(
        summary="Создать сотрудника",
        description="Создание нового сотрудника (администратор)",
        tags=[APISchemaTags.EMPLOYEES],
        request=EmployeeRequestSerializer,
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_201_CREATED: EmployeeRequestSerializer},
    ),
    list=extend_schema(
        summary="Получить список сотрудников",
        description="Возвращает список сотрудников (включая паспорт, рабочее место и группы)",
        tags=[APISchemaTags.EMPLOYEES],
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_200_OK: EmployeeRequestSerializer(many=True)},
    ),
    retrieve=extend_schema(
        summary="Получить сотрудника по ID",
        description="Детальная информация по сотруднику",
        tags=[APISchemaTags.EMPLOYEES],
        parameters=[OpenApiParameter(name="id", description="ID сотрудника", required=True, type=int, location=OpenApiParameter.PATH)],
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_200_OK: EmployeeRequestSerializer},
    ),
    update=extend_schema(
        summary="Обновить сотрудника",
        description="Полное обновление данных сотрудника",
        tags=[APISchemaTags.EMPLOYEES],
        request=EmployeeRequestSerializer,
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_200_OK: EmployeeRequestSerializer},
    ),
    partial_update=extend_schema(
        summary="Частично обновить сотрудника",
        description="Частичное обновление данных сотрудника",
        tags=[APISchemaTags.EMPLOYEES],
        request=EmployeeRequestSerializer,
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_200_OK: EmployeeRequestSerializer},
    ),
    destroy=extend_schema(
        summary="Удалить сотрудника",
        description="Удаление сотрудника из системы",
        tags=[APISchemaTags.EMPLOYEES],
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_204_NO_CONTENT: None},
    ),
)
class EmployeeViewSet(viewsets.ModelViewSet):
    """CRUD операции для сотрудников"""
    authentication_classes = [JWTAuthentication]
    queryset = Employee.objects.select_related("passport", "workplace__storage", "workplace__main_office_filial").all()
    serializer_class = EmployeeRequestSerializer
    lookup_field = "id"

    def get_permissions(self):
        # read access for authenticated users; write/delete only for main office (admin)
        if self.action in ["list", "retrieve"]:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated, HasMainOfficeGroupPermission]
        return [p() for p in permission_classes]


@extend_schema_view(
    create=extend_schema(
        summary="Создать тип запроса на отсутствие",
        description="Создание типа запроса на временное отсутствие",
        tags=[APISchemaTags.EMPLOYEES],
        request=LeaveRequestTypeRequestSerializer,
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_201_CREATED: LeaveRequestTypeRequestSerializer},
    ),
    list=extend_schema(
        summary="Получить список типов запросов на отсутствие",
        description="Справочник типов временных отсутствий",
        tags=[APISchemaTags.EMPLOYEES],
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_200_OK: LeaveRequestTypeRequestSerializer(many=True)},
    ),
    retrieve=extend_schema(
        summary="Получить тип запроса на отсутствие по ID",
        description="Детальная информация по типу запроса",
        tags=[APISchemaTags.EMPLOYEES],
        parameters=[OpenApiParameter(name="id", description="ID типа", required=True, type=int, location=OpenApiParameter.PATH)],
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_200_OK: LeaveRequestTypeRequestSerializer},
    ),
    update=extend_schema(
        summary="Обновить тип запроса на отсутствие",
        description="Полное обновление типа запроса",
        tags=[APISchemaTags.EMPLOYEES],
        request=LeaveRequestTypeRequestSerializer,
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_200_OK: LeaveRequestTypeRequestSerializer},
    ),
    partial_update=extend_schema(
        summary="Частично обновить тип запроса на отсутствие",
        description="Частичное обновление типа запроса",
        tags=[APISchemaTags.EMPLOYEES],
        request=LeaveRequestTypeRequestSerializer,
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_200_OK: LeaveRequestTypeRequestSerializer},
    ),
    destroy=extend_schema(
        summary="Удалить тип запроса на отсутствие",
        description="Удаление типа запроса",
        tags=[APISchemaTags.EMPLOYEES],
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_204_NO_CONTENT: None},
    ),
)
class LeaveRequestTypeViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    queryset = LeaveRequestType.objects.all()
    serializer_class = LeaveRequestTypeRequestSerializer
    lookup_field = "id"

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated, HasMainOfficeGroupPermission]
        return [p() for p in permission_classes]


@extend_schema_view(
    create=extend_schema(
        summary="Создать запрос на временное отсутствие",
        description="Создание запроса на отпуск/больничный (пользователь может создать собственный запрос)",
        tags=[APISchemaTags.EMPLOYEES],
        request=LeaveRequestRequestSerializer,
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_201_CREATED: LeaveRequestRequestSerializer},
    ),
    list=extend_schema(
        summary="Получить список запросов на отсутствие",
        description="Возвращает список запросов на отсутствие",
        tags=[APISchemaTags.EMPLOYEES],
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_200_OK: LeaveRequestRequestSerializer(many=True)},
    ),
    retrieve=extend_schema(
        summary="Получить запрос на отсутствие по ID",
        description="Детальная информация по запросу на отсутствие",
        tags=[APISchemaTags.EMPLOYEES],
        parameters=[OpenApiParameter(name="id", description="ID запроса", required=True, type=int, location=OpenApiParameter.PATH)],
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_200_OK: LeaveRequestRequestSerializer},
    ),
    update=extend_schema(
        summary="Обновить запрос на отсутствие",
        description="Обновление запроса (обычно разрешено менеджерам/админам)",
        tags=[APISchemaTags.EMPLOYEES],
        request=LeaveRequestRequestSerializer,
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_200_OK: LeaveRequestRequestSerializer},
    ),
    partial_update=extend_schema(
        summary="Частично обновить запрос на отсутствие",
        description="Частичное обновление запроса",
        tags=[APISchemaTags.EMPLOYEES],
        request=LeaveRequestRequestSerializer,
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_200_OK: LeaveRequestRequestSerializer},
    ),
    destroy=extend_schema(
        summary="Удалить запрос на отсутствие",
        description="Удаление запроса на отсутствие",
        tags=[APISchemaTags.EMPLOYEES],
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_204_NO_CONTENT: None},
    ),
)
class LeaveRequestViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    queryset = LeaveRequest.objects.select_related("employee", "approved_by").prefetch_related("attachments").all()
    serializer_class = LeaveRequestRequestSerializer
    lookup_field = "id"

    def get_permissions(self):
        # anyone authenticated can create and list/retrieve their own requests;
        # modifying/deleting requires main-office permission
        if self.action in ["create", "list", "retrieve"]:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated, HasMainOfficeGroupPermission]
        return [p() for p in permission_classes]

    def get_queryset(self):
        qs = super().get_queryset()
        # non-staff users see only their own leave requests by default
        user = getattr(self.request, "user", None)
        if user and not (user.is_staff or user.is_superuser):
            qs = qs.filter(employee_id=user.pk)
        return qs


@extend_schema_view(
    create=extend_schema(
        summary="Добавить вложение к запросу на отсутствие",
        description="Загрузка файла-вложения для запроса на отсутствие",
        tags=[APISchemaTags.EMPLOYEES],
        request=LeaveRequestAttachmentRequestSerializer,
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_201_CREATED: LeaveRequestAttachmentRequestSerializer},
    ),
    list=extend_schema(
        summary="Получить список вложений для запросов на отсутствие",
        description="Список вложений; можно фильтровать по leave_request (id)",
        tags=[APISchemaTags.EMPLOYEES],
        parameters=[
            OpenApiParameter(name="leave_request", description="ID запроса", required=False, type=int, location=OpenApiParameter.QUERY)
        ],
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_200_OK: LeaveRequestAttachmentRequestSerializer(many=True)},
    ),
    retrieve=extend_schema(
        summary="Получить вложение по ID",
        description="Детальная информация по вложению",
        tags=[APISchemaTags.EMPLOYEES],
        parameters=[OpenApiParameter(name="id", description="ID вложения", required=True, type=int, location=OpenApiParameter.PATH)],
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_200_OK: LeaveRequestAttachmentRequestSerializer},
    ),
    destroy=extend_schema(
        summary="Удалить вложение",
        description="Удаление вложения",
        tags=[APISchemaTags.EMPLOYEES],
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_204_NO_CONTENT: None},
    ),
)
class LeaveRequestAttachmentViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    queryset = LeaveRequestAttachment.objects.select_related("leave_request").all()
    serializer_class = LeaveRequestAttachmentRequestSerializer
    lookup_field = "id"

    def get_permissions(self):
        # authenticated users can upload attachments; deletion restricted
        if self.action in ["create", "list", "retrieve"]:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated, HasMainOfficeGroupPermission]
        return [p() for p in permission_classes]

    def get_queryset(self):
        qs = super().get_queryset()
        leave_request_id = self.request.query_params.get("leave_request")
        if leave_request_id:
            qs = qs.filter(leave_request_id=leave_request_id)
        # non-staff users see only attachments for their own leave requests
        user = getattr(self.request, "user", None)
        if user and not (user.is_staff or user.is_superuser):
            qs = qs.filter(leave_request__employee_id=user.pk)
        return qs


@extend_schema_view(
    create=extend_schema(
        summary="Создать баланс отпусков",
        description="Создание/корректировка годового баланса отпуска для сотрудника",
        tags=[APISchemaTags.EMPLOYEES],
        request=AnnualLeaveBalanceRequestSerializer,
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_201_CREATED: AnnualLeaveBalanceRequestSerializer},
    ),
    list=extend_schema(
        summary="Получить список отпускных балансов",
        description="Список отпускных балансов по сотрудникам",
        tags=[APISchemaTags.EMPLOYEES],
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_200_OK: AnnualLeaveBalanceRequestSerializer(many=True)},
    ),
    retrieve=extend_schema(
        summary="Получить отпускной баланс по ID",
        description="Детальная информация по отпускному балансу",
        tags=[APISchemaTags.EMPLOYEES],
        parameters=[OpenApiParameter(name="id", description="ID записи", required=True, type=int, location=OpenApiParameter.PATH)],
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_200_OK: AnnualLeaveBalanceRequestSerializer},
    ),
    update=extend_schema(
        summary="Обновить отпускной баланс",
        description="Обновление записи отпускного баланса",
        tags=[APISchemaTags.EMPLOYEES],
        request=AnnualLeaveBalanceRequestSerializer,
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_200_OK: AnnualLeaveBalanceRequestSerializer},
    ),
    partial_update=extend_schema(
        summary="Частично обновить отпускной баланс",
        description="Частичное обновление записи отпускного баланса",
        tags=[APISchemaTags.EMPLOYEES],
        request=AnnualLeaveBalanceRequestSerializer,
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_200_OK: AnnualLeaveBalanceRequestSerializer},
    ),
    destroy=extend_schema(
        summary="Удалить отпускной баланс",
        description="Удаление записи отпускного баланса",
        tags=[APISchemaTags.EMPLOYEES],
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_204_NO_CONTENT: None},
    ),
)
class AnnualLeaveBalanceViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    queryset = AnnualLeaveBalance.objects.select_related("employee").all()
    serializer_class = AnnualLeaveBalanceRequestSerializer
    lookup_field = "id"

    def get_permissions(self):
        # only main office can modify balances; read allowed for authenticated
        if self.action in ["list", "retrieve"]:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated, HasMainOfficeGroupPermission]
        return [p() for p in permission_classes]


@extend_schema_view(
    create=extend_schema(
        summary="Создать списание времени (TimeEntry)",
        description="Создание записи списания времени сотрудника",
        tags=[APISchemaTags.EMPLOYEES],
        request=TimeEntryRequestSerializer,
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_201_CREATED: TimeEntryRequestSerializer},
    ),
    list=extend_schema(
        summary="Получить список списаний времени",
        description="Список списаний времени; можно фильтровать по employee",
        tags=[APISchemaTags.EMPLOYEES],
        parameters=[OpenApiParameter(name="employee", description="ID сотрудника", required=False, type=int, location=OpenApiParameter.QUERY)],
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_200_OK: TimeEntryRequestSerializer(many=True)},
    ),
    retrieve=extend_schema(
        summary="Получить списание времени по ID",
        description="Детальная информация по списанию времени",
        tags=[APISchemaTags.EMPLOYEES],
        parameters=[OpenApiParameter(name="id", description="ID записи", required=True, type=int, location=OpenApiParameter.PATH)],
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_200_OK: TimeEntryRequestSerializer},
    ),
    update=extend_schema(
        summary="Обновить списание времени",
        description="Обновление записи списания времени (обычно админы)",
        tags=[APISchemaTags.EMPLOYEES],
        request=TimeEntryRequestSerializer,
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_200_OK: TimeEntryRequestSerializer},
    ),
    partial_update=extend_schema(
        summary="Частично обновить списание времени",
        description="Частичное обновление записи списания времени",
        tags=[APISchemaTags.EMPLOYEES],
        request=TimeEntryRequestSerializer,
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_200_OK: TimeEntryRequestSerializer},
    ),
    destroy=extend_schema(
        summary="Удалить списание времени",
        description="Удаление записи списания времени",
        tags=[APISchemaTags.EMPLOYEES],
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_204_NO_CONTENT: None},
    ),
)
class TimeEntryViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    queryset = TimeEntry.objects.select_related("employee").all()
    serializer_class = TimeEntryRequestSerializer
    lookup_field = "id"

    def get_permissions(self):
        # allow create/list/retrieve for authenticated users; modify/delete restricted
        if self.action in ["create", "list", "retrieve"]:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated, HasMainOfficeGroupPermission]
        return [p() for p in permission_classes]

    def get_queryset(self):
        qs = super().get_queryset()
        employee_id = self.request.query_params.get("employee")
        if employee_id:
            qs = qs.filter(employee_id=employee_id)
        user = getattr(self.request, "user", None)
        # non-staff users see only their own time entries
        if user and not (user.is_staff or user.is_superuser):
            qs = qs.filter(employee_id=user.pk)
        return qs


@extend_schema_view(
    create=extend_schema(
        summary="Создать причину закрытия сессии",
        description="Создание причины закрытия рабочей сессии",
        tags=[APISchemaTags.EMPLOYEES],
        request=TimeSessionCloseReasonRequestSerializer,
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_201_CREATED: TimeSessionCloseReasonRequestSerializer},
    ),
    list=extend_schema(
        summary="Получить список причин закрытия сессии",
        description="Справочник причин закрытия сессии",
        tags=[APISchemaTags.EMPLOYEES],
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_200_OK: TimeSessionCloseReasonRequestSerializer(many=True)},
    ),
    retrieve=extend_schema(
        summary="Получить причину закрытия сессии по ID",
        description="Детальная информация по причине закрытия сессии",
        tags=[APISchemaTags.EMPLOYEES],
        parameters=[OpenApiParameter(name="id", description="ID записи", required=True, type=int, location=OpenApiParameter.PATH)],
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_200_OK: TimeSessionCloseReasonRequestSerializer},
    ),
    update=extend_schema(
        summary="Обновить причину закрытия сессии",
        description="Полное обновление причины закрытия сессии",
        tags=[APISchemaTags.EMPLOYEES],
        request=TimeSessionCloseReasonRequestSerializer,
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_200_OK: TimeSessionCloseReasonRequestSerializer},
    ),
    partial_update=extend_schema(
        summary="Частично обновить причину закрытия сессии",
        description="Частичное обновление причины закрытия сессии",
        tags=[APISchemaTags.EMPLOYEES],
        request=TimeSessionCloseReasonRequestSerializer,
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_200_OK: TimeSessionCloseReasonRequestSerializer},
    ),
    destroy=extend_schema(
        summary="Удалить причину закрытия сессии",
        description="Удаление записи причины закрытия сессии",
        tags=[APISchemaTags.EMPLOYEES],
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_204_NO_CONTENT: None},
    ),
)
class TimeSessionCloseReasonViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    queryset = TimeSessionCloseReason.objects.all()
    serializer_class = TimeSessionCloseReasonRequestSerializer
    lookup_field = "id"

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated, HasMainOfficeGroupPermission]
        return [p() for p in permission_classes]


@extend_schema_view(
    create=extend_schema(
        summary="Создать рабочую сессию",
        description="Создание рабочей сессии (логин/логаут)",
        tags=[APISchemaTags.EMPLOYEES],
        request=TimeSessionRequestSerializer,
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_201_CREATED: TimeSessionRequestSerializer},
    ),
    list=extend_schema(
        summary="Получить список рабочих сессий",
        description="Список рабочих сессий; можно фильтровать по employee",
        tags=[APISchemaTags.EMPLOYEES],
        parameters=[OpenApiParameter(name="employee", description="ID сотрудника", required=False, type=int, location=OpenApiParameter.QUERY)],
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_200_OK: TimeSessionRequestSerializer(many=True)},
    ),
    retrieve=extend_schema(
        summary="Получить рабочую сессию по ID",
        description="Детальная информация по рабочей сессии",
        tags=[APISchemaTags.EMPLOYEES],
        parameters=[OpenApiParameter(name="id", description="ID записи", required=True, type=int, location=OpenApiParameter.PATH)],
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_200_OK: TimeSessionRequestSerializer},
    ),
    update=extend_schema(
        summary="Обновить рабочую сессию",
        description="Обновление записи рабочей сессии",
        tags=[APISchemaTags.EMPLOYEES],
        request=TimeSessionRequestSerializer,
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_200_OK: TimeSessionRequestSerializer},
    ),
    partial_update=extend_schema(
        summary="Частично обновить рабочую сессию",
        description="Частичное обновление записи рабочей сессии",
        tags=[APISchemaTags.EMPLOYEES],
        request=TimeSessionRequestSerializer,
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_200_OK: TimeSessionRequestSerializer},
    ),
    destroy=extend_schema(
        summary="Удалить рабочую сессию",
        description="Удаление записи рабочей сессии",
        tags=[APISchemaTags.EMPLOYEES],
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_204_NO_CONTENT: None},
    ),
)
class TimeSessionViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    queryset = TimeSession.objects.select_related("employee", "close_reason").all()
    serializer_class = TimeSessionRequestSerializer
    lookup_field = "id"

    def get_permissions(self):
        # create/list/retrieve allowed for authenticated users; modify/delete restricted
        if self.action in ["create", "list", "retrieve"]:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated, HasMainOfficeGroupPermission]
        return [p() for p in permission_classes]

    def get_queryset(self):
        qs = super().get_queryset()
        employee_id = self.request.query_params.get("employee")
        if employee_id:
            qs = qs.filter(employee_id=employee_id)
        user = getattr(self.request, "user", None)
        if user and not (user.is_staff or user.is_superuser):
            qs = qs.filter(employee_id=user.pk)
        return qs


@extend_schema_view(
    create=extend_schema(
        summary="Создать сводку по дню (TimeDay)",
        description="Создание/обновление сводки по дню работника",
        tags=[APISchemaTags.EMPLOYEES],
        request=TimeDayRequestSerializer,
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_201_CREATED: TimeDayRequestSerializer},
    ),
    list=extend_schema(
        summary="Получить список сводок по дням",
        description="Список сводок по дням; можно фильтровать по employee и date",
        tags=[APISchemaTags.EMPLOYEES],
        parameters=[
            OpenApiParameter(name="employee", description="ID сотрудника", required=False, type=int, location=OpenApiParameter.QUERY),
            OpenApiParameter(name="date", description="Дата в формате YYYY-MM-DD", required=False, type=str, location=OpenApiParameter.QUERY),
        ],
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_200_OK: TimeDayRequestSerializer(many=True)},
    ),
    retrieve=extend_schema(
        summary="Получить сводку по дню по ID",
        description="Детальная информация по сводке по дню",
        tags=[APISchemaTags.EMPLOYEES],
        parameters=[OpenApiParameter(name="id", description="ID записи", required=True, type=int, location=OpenApiParameter.PATH)],
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_200_OK: TimeDayRequestSerializer},
    ),
    update=extend_schema(
        summary="Обновить сводку по дню",
        description="Обновление сводки по дню",
        tags=[APISchemaTags.EMPLOYEES],
        request=TimeDayRequestSerializer,
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_200_OK: TimeDayRequestSerializer},
    ),
    partial_update=extend_schema(
        summary="Частично обновить сводку по дню",
        description="Частичное обновление сводки по дню",
        tags=[APISchemaTags.EMPLOYEES],
        request=TimeDayRequestSerializer,
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_200_OK: TimeDayRequestSerializer},
    ),
    destroy=extend_schema(
        summary="Удалить сводку по дню",
        description="Удаление записи сводки по дню",
        tags=[APISchemaTags.EMPLOYEES],
        responses={**DefaultAPIResponses.RESPONSES, status.HTTP_204_NO_CONTENT: None},
    ),
)
class TimeDayViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    queryset = TimeDay.objects.select_related("employee", "adjustment_reason").all()
    serializer_class = TimeDayRequestSerializer
    lookup_field = "id"

    def get_permissions(self):
        # allow create/list/retrieve for authenticated users; modify/delete restricted
        if self.action in ["create", "list", "retrieve"]:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated, HasMainOfficeGroupPermission]
        return [p() for p in permission_classes]

    def get_queryset(self):
        qs = super().get_queryset()
        employee_id = self.request.query_params.get("employee")
        date = self.request.query_params.get("date")
        if employee_id:
            qs = qs.filter(employee_id=employee_id)
        if date:
            qs = qs.filter(date=date)
        user = getattr(self.request, "user", None)
        if user and not (user.is_staff or user.is_superuser):
            qs = qs.filter(employee_id=user.pk)
        return qs


class UserGroupsView(APIView):

    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    @extend_schema(
        summary='Получить группы пользователя',
        description=(
            'Возвращает список групп пользователя по его ID.\n\n'
            'Формат ответа:\n'
            '{ "<user_id>": ["group1", "group2"] }'
        ),
        parameters=[
            OpenApiParameter(
                name='user_id',
                type=int,
                location=OpenApiParameter.QUERY,
                description='ID пользователя (Employee)',
            ),
        ],
        responses={
            200: OpenApiResponse(
                description='Список групп пользователя',
                examples=[
                    OpenApiExample(
                        'Ответ',
                        value={
                            "123": ["director_group", "manager"],
                        },
                    ),
                ],
            ),
            401: OpenApiResponse(description='Неавторизован'),
        },
        tags=[APISchemaTags.EMPLOYEES],
    )
    def get(self, request):
        user_id = request.query_params.get('user_id')
        data = get_user_groups(user_id)
        return Response(status=status.HTTP_200_OK, data=data)
