from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter
from rest_framework import status, viewsets, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from common_utils.constants import APISchemaTags, DefaultAPIResponses
from common_utils.permissions import HasMainOfficeGroupPermission

from supplies.models import Supplier, SupplierContact, SupplyContract, SupplyContractProduct
from supplies.serializers import (
    SupplierRequestSerializer,
    SupplierContactRequestSerializer,
    SupplyContractRequestSerializer,
    SupplyContractProductRequestSerializer,
)


# ---------- SUPPLIERS ----------

@extend_schema_view(
    list=extend_schema(
        summary="Список поставщиков",
        tags=[APISchemaTags.SUPPLIES],
        parameters=[
            OpenApiParameter(
                name="search",
                required=False,
                type=str,
                description="Поиск по поставщикам (name/inn/ogrn)",
            )
        ],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: SupplierRequestSerializer(many=True),
        },
    ),
    retrieve=extend_schema(
        summary="Поставщик по ID",
        tags=[APISchemaTags.SUPPLIES],
        parameters=[OpenApiParameter(name="id", required=True, type=int, location=OpenApiParameter.PATH)],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: SupplierRequestSerializer,
        },
    ),
    create=extend_schema(
        summary="Создать поставщика",
        tags=[APISchemaTags.SUPPLIES],
        request=SupplierRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_201_CREATED: SupplierRequestSerializer,
        },
    ),
    update=extend_schema(
        summary="Обновить поставщика",
        tags=[APISchemaTags.SUPPLIES],
        request=SupplierRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: SupplierRequestSerializer,
        },
    ),
    partial_update=extend_schema(
        summary="Частично обновить поставщика",
        tags=[APISchemaTags.SUPPLIES],
        request=SupplierRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: SupplierRequestSerializer,
        },
    ),
    destroy=extend_schema(
        summary="Удалить поставщика",
        tags=[APISchemaTags.SUPPLIES],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_204_NO_CONTENT: None,
        },
    ),
)
class SupplierViewSet(viewsets.ModelViewSet):
    """CRUD операции для поставщиков"""

    authentication_classes = [JWTAuthentication]
    queryset = Supplier.objects.all()
    serializer_class = SupplierRequestSerializer
    lookup_field = "id"

    filter_backends = [filters.SearchFilter]
    search_fields = ["name", "inn", "ogrn"]

    def get_permissions(self):
        # чтение всем авторизованным, запись только ГК (main_office_group) или суперюзер
        if self.action in ["list", "retrieve"]:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated, HasMainOfficeGroupPermission]
        return [p() for p in permission_classes]


# ---------- SUPPLIER CONTACTS ----------

@extend_schema_view(
    list=extend_schema(
        summary="Список контактных лиц поставщиков",
        tags=[APISchemaTags.SUPPLIES],
        parameters=[
            OpenApiParameter(
                name="supplier",
                required=False,
                type=int,
                description="Фильтр по supplier_id",
            )
        ],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: SupplierContactRequestSerializer(many=True),
        },
    ),
    retrieve=extend_schema(
        summary="Контактное лицо по ID",
        tags=[APISchemaTags.SUPPLIES],
        parameters=[OpenApiParameter(name="id", required=True, type=int, location=OpenApiParameter.PATH)],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: SupplierContactRequestSerializer,
        },
    ),
    create=extend_schema(
        summary="Создать контактное лицо поставщика",
        tags=[APISchemaTags.SUPPLIES],
        request=SupplierContactRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_201_CREATED: SupplierContactRequestSerializer,
        },
    ),
    update=extend_schema(
        summary="Обновить контактное лицо",
        tags=[APISchemaTags.SUPPLIES],
        request=SupplierContactRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: SupplierContactRequestSerializer,
        },
    ),
    partial_update=extend_schema(
        summary="Частично обновить контактное лицо",
        tags=[APISchemaTags.SUPPLIES],
        request=SupplierContactRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: SupplierContactRequestSerializer,
        },
    ),
    destroy=extend_schema(
        summary="Удалить контактное лицо",
        tags=[APISchemaTags.SUPPLIES],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_204_NO_CONTENT: None,
        },
    ),
)
class SupplierContactViewSet(viewsets.ModelViewSet):
    """CRUD операции для контактных лиц поставщиков"""

    authentication_classes = [JWTAuthentication]
    queryset = SupplierContact.objects.all()
    serializer_class = SupplierContactRequestSerializer
    lookup_field = "id"

    def get_queryset(self):
        qs = super().get_queryset()
        supplier_id = self.request.query_params.get("supplier")
        return qs.filter(supplier_id=supplier_id) if supplier_id else qs

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated, HasMainOfficeGroupPermission]
        return [p() for p in permission_classes]


# ---------- CONTRACTS ----------

@extend_schema_view(
    list=extend_schema(
        summary="Список договоров поставки",
        tags=[APISchemaTags.SUPPLIES],
        parameters=[
            OpenApiParameter(
                name="supplier",
                required=False,
                type=int,
                description="Фильтр по supplier_id",
            )
        ],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: SupplyContractRequestSerializer(many=True),
        },
    ),
    retrieve=extend_schema(
        summary="Договор по ID",
        tags=[APISchemaTags.SUPPLIES],
        parameters=[OpenApiParameter(name="id", required=True, type=int, location=OpenApiParameter.PATH)],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: SupplyContractRequestSerializer,
        },
    ),
    create=extend_schema(
        summary="Создать договор поставки",
        tags=[APISchemaTags.SUPPLIES],
        request=SupplyContractRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_201_CREATED: SupplyContractRequestSerializer,
        },
    ),
    update=extend_schema(
        summary="Обновить договор поставки",
        tags=[APISchemaTags.SUPPLIES],
        request=SupplyContractRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: SupplyContractRequestSerializer,
        },
    ),
    partial_update=extend_schema(
        summary="Частично обновить договор поставки",
        tags=[APISchemaTags.SUPPLIES],
        request=SupplyContractRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: SupplyContractRequestSerializer,
        },
    ),
    destroy=extend_schema(
        summary="Удалить договор поставки",
        tags=[APISchemaTags.SUPPLIES],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_204_NO_CONTENT: None,
        },
    ),
)
class SupplyContractViewSet(viewsets.ModelViewSet):
    """CRUD операции для договоров на поставки"""

    authentication_classes = [JWTAuthentication]
    queryset = SupplyContract.objects.all()
    serializer_class = SupplyContractRequestSerializer
    lookup_field = "id"

    def get_queryset(self):
        qs = super().get_queryset()
        supplier_id = self.request.query_params.get("supplier")
        return qs.filter(supplier_id=supplier_id) if supplier_id else qs

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated, HasMainOfficeGroupPermission]
        return [p() for p in permission_classes]


# ---------- CONTRACT PRODUCTS ----------

@extend_schema_view(
    list=extend_schema(
        summary="Список товаров в договоре поставки",
        tags=[APISchemaTags.SUPPLIES],
        parameters=[
            OpenApiParameter(
                name="contract",
                required=False,
                type=int,
                description="Фильтр по supply_contract_id",
            )
        ],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: SupplyContractProductRequestSerializer(many=True),
        },
    ),
    retrieve=extend_schema(
        summary="Товар договора по ID",
        tags=[APISchemaTags.SUPPLIES],
        parameters=[OpenApiParameter(name="id", required=True, type=int, location=OpenApiParameter.PATH)],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: SupplyContractProductRequestSerializer,
        },
    ),
    create=extend_schema(
        summary="Добавить товар в договор",
        tags=[APISchemaTags.SUPPLIES],
        request=SupplyContractProductRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_201_CREATED: SupplyContractProductRequestSerializer,
        },
    ),
    update=extend_schema(
        summary="Обновить товар в договоре",
        tags=[APISchemaTags.SUPPLIES],
        request=SupplyContractProductRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: SupplyContractProductRequestSerializer,
        },
    ),
    partial_update=extend_schema(
        summary="Частично обновить товар в договоре",
        tags=[APISchemaTags.SUPPLIES],
        request=SupplyContractProductRequestSerializer,
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_200_OK: SupplyContractProductRequestSerializer,
        },
    ),
    destroy=extend_schema(
        summary="Удалить товар из договора",
        tags=[APISchemaTags.SUPPLIES],
        responses={
            **DefaultAPIResponses.RESPONSES,
            status.HTTP_204_NO_CONTENT: None,
        },
    ),
)
class SupplyContractProductViewSet(viewsets.ModelViewSet):
    """CRUD операции для товаров в договоре поставки"""

    authentication_classes = [JWTAuthentication]
    queryset = SupplyContractProduct.objects.all()
    serializer_class = SupplyContractProductRequestSerializer
    lookup_field = "id"

    def get_queryset(self):
        qs = super().get_queryset()
        contract_id = self.request.query_params.get("contract")
        return qs.filter(supply_contract_id=contract_id) if contract_id else qs

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated, HasMainOfficeGroupPermission]
        return [p() for p in permission_classes]