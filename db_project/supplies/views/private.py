from django.db import transaction
from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter
from rest_framework import status, viewsets, filters, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework_simplejwt.authentication import JWTAuthentication

from common_utils.constants import APISchemaTags, DefaultAPIResponses
from common_utils.permissions import (
    HasMainOfficeGroupPermission,
    HasCommodityExpertGroupPermission,
    HasStorekeeperGroupPermission,
    HasDirectorGroupPermission,
)

from supplies.models import (
    Supplier, SupplierContact, SupplyContract, SupplyContractProduct,
    Supply, SupplyProduct, SupplyProductLot,
    DiscrepancyReason, SupplyDiscrepancy, DiscrepancyAttachment,
)
from supplies.serializers import (
    SupplierRequestSerializer,
    SupplierContactRequestSerializer,
    SupplyContractRequestSerializer,
    SupplyContractProductRequestSerializer,
    
    SupplyRequestSerializer,
    SupplyProductRequestSerializer,
    SupplyProductLotRequestSerializer,
    DiscrepancyReasonRequestSerializer,
    SupplyDiscrepancyRequestSerializer,
    DiscrepancyAttachmentRequestSerializer,
    DecisionSerializer
)
from supplies.services.workflow import set_discrepancy_decision
from supplies.services.posting import post_supply_to_inventory


class HasSuppliesWorkflowWritePermission(permissions.BasePermission):
    """
    Пишем в supplies workflow: ГК / товаровед / кладовщик / директор (или суперюзер)
    """
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        return request.user.groups.filter(
            name__in=[
                "main_office_group",
                "commodity_expert_group",
                "storekeeper_group",
                "director_group",
            ]
        ).exists()

def _as_bool(value):
    if value is None:
        return None
    v = str(value).strip().lower()
    if v in ("1", "true", "yes", "y", "on"):
        return True
    if v in ("0", "false", "no", "n", "off"):
        return False
    return None

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

    
# ---------- SUPPLIES (Документ поставки) ----------
    
@extend_schema_view(
    list=extend_schema(
        summary="Список поставок",
        tags=[APISchemaTags.SUPPLIES],
        parameters=[
            OpenApiParameter(name="status", required=False, type=str, description="Фильтр по status"),
            OpenApiParameter(name="storage", required=False, type=int, description="Фильтр по storage_id"),
            OpenApiParameter(name="supply_contract", required=False, type=int, description="Фильтр по supply_contract_id"),
            OpenApiParameter(name="created_by", required=False, type=int, description="Фильтр по created_by (employee_id)"),
            OpenApiParameter(name="received_by", required=False, type=int, description="Фильтр по received_by (employee_id)"),
            OpenApiParameter(name="planned_date_from", required=False, type=str, description="planned_date >= YYYY-MM-DD"),
            OpenApiParameter(name="planned_date_to", required=False, type=str, description="planned_date <= YYYY-MM-DD"),
        ],
    ),
    retrieve=extend_schema(summary="Детали поставки", tags=[APISchemaTags.SUPPLIES]),
    create=extend_schema(summary="Создать поставку", tags=[APISchemaTags.SUPPLIES]),
    update=extend_schema(summary="Обновить поставку", tags=[APISchemaTags.SUPPLIES]),
    partial_update=extend_schema(summary="Частично обновить поставку", tags=[APISchemaTags.SUPPLIES]),
    destroy=extend_schema(summary="Удалить поставку", tags=[APISchemaTags.SUPPLIES]),
)
class SupplyViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    queryset = Supply.objects.all()
    serializer_class = SupplyRequestSerializer
    lookup_field = "id"
    
    def get_queryset(self):
        qs = super().get_queryset()
        p = self.request.query_params
        
        if p.get("status"):
            qs = qs.filter(status=p["status"])
        if p.get("storage"):
            qs = qs.filter(storage_id=p["storage"])
        if p.get("supply_contract"):
            qs = qs.filter(supply_contract_id=p["supply_contract"])
        if p.get("created_by"):
            qs = qs.filter(created_by_id=p["created_by"])
        if p.get("received_by"):
            qs = qs.filter(received_by_id=p["received_by"])
        if p.get("planned_date_from"):
            qs = qs.filter(planned_date__gte=p["planned_date_from"])
        if p.get("planned_date_to"):
            qs = qs.filter(planned_date__lte=p["planned_date_to"])
            
        return qs
    
    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated, HasSuppliesWorkflowWritePermission]
        return [p() for p in permission_classes]
    
    # --- MIN: populate supply products from contract ---
    @extend_schema(
        summary="Заполнить поставку продуктами из договора",
        description=(
            "Создаёт строки SupplyProduct по всем SupplyContractProduct из supply.supply_contract.\n"
            "Идемпотентно: повторный вызов не создаёт дубли."
        ),
        tags=[APISchemaTags.SUPPLIES],
        request=None,
        responses={200: dict},
    )
    @action(detail=True, methods=["post"], url_path="populate-from-contract")
    def populate_from_contract(self, request, pk=None):
        supply = self.get_object()
        
        # Не плодим мусор в “закрытом” документе
        if supply.status in (Supply.APPROVED, Supply.REJECTED, Supply.CLOSED):
            return Response(
                {"detail": "Нельзя заполнять поставку в статусе approved/rejected/closed"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        
        contract_products = SupplyContractProduct.objects.select_related("product").filter(
            supply_contract_id=supply.supply_contract_id
        )
        
        existing_cp_ids = set(
            SupplyProduct.objects.filter(supply_id=supply.id)
            .values_list("supply_contract_product_id", flat=True)
        )
        
        to_create = []
        skipped = 0
        
        for cp in contract_products:
            if cp.id in existing_cp_ids:
                skipped += 1
                continue
            
            to_create.append(
                SupplyProduct(
                    supply=supply,
                    product=cp.product,
                    supply_contract_product=cp,
                    quantity_actual_total=0,          # обязателен в модели
                    quantity_expected=cp.quantity,
                    requires_review=True,
                    status=SupplyProduct.HAS_ISSUES,
                    purchase_price=cp.price,
                )
            )
            
        with transaction.atomic():
            if to_create:
                SupplyProduct.objects.bulk_create(to_create)
                
        return Response(
            {
                "detail": "SupplyProduct созданы из договора",
                "supply_id": supply.id,
                "contract_id": supply.supply_contract_id,
                "created": len(to_create),
                "skipped_existing": skipped,
                "total_in_contract": contract_products.count(),
            },
            status=status.HTTP_200_OK,
        )
    
    # --- workflow actions (как у тебя было) ---
    @extend_schema(summary="Начать приёмку (draft -> in_receiving)", request=None, responses={200: None})
    @action(detail=True, methods=["post"], url_path="start-receiving",
            permission_classes=[HasStorekeeperGroupPermission | HasCommodityExpertGroupPermission | HasMainOfficeGroupPermission])
    def start_receiving(self, request, pk=None):
        supply = self.get_object()
        if supply.status != Supply.DRAFT:
            return Response({"detail": "Нельзя начать приёмку не из draft"}, status=400)
        supply.status = Supply.IN_RECEIVING
        supply.received_by = getattr(request.user, "employee", None)
        supply.save(update_fields=["status", "received_by"])
        return Response(status=200)
    
    
    @extend_schema(summary="Отправить в ГК (in_receiving -> pending_approval)", request=None, responses={200: None})
    @action(detail=True, methods=["post"], url_path="submit-to-hq",
            permission_classes=[HasCommodityExpertGroupPermission | HasMainOfficeGroupPermission])
    def submit_to_hq(self, request, pk=None):
        supply = self.get_object()
        if supply.status != Supply.IN_RECEIVING:
            return Response({"detail": "Нельзя отправить в ГК не из in_receiving"}, status=400)
        supply.status = Supply.PENDING_APPROVAL
        supply.save(update_fields=["status"])
        return Response(status=200)
    
    
    @extend_schema(summary="Одобрить (pending_approval -> approved)", request=None, responses={200: None})
    @action(detail=True, methods=["post"], url_path="approve", permission_classes=[HasMainOfficeGroupPermission])
    def approve(self, request, pk=None):
        supply = self.get_object()
        if supply.status != Supply.PENDING_APPROVAL:
            return Response({"detail": "Нельзя approve не из pending_approval"}, status=400)
        
        supply.status = Supply.APPROVED
        supply.save(update_fields=["status"])
        
        actor_employee = getattr(request.user, "employee", None) or supply.received_by or supply.created_by
        result = post_supply_to_inventory(supply, actor_employee)
        
        return Response(
            {
                "detail": "Поставка проведена",
                "created_inventory_lots": result.created_inventory_lots,
                "created_balances": result.created_balances,
                "created_movements": result.created_movements,
            },
            status=200,
        )
    
    
    @extend_schema(summary="Отклонить (pending_approval -> rejected)", request=DecisionSerializer, responses={200: None})
    @action(detail=True, methods=["post"], url_path="reject",
            permission_classes=[HasMainOfficeGroupPermission])
    def reject(self, request, pk=None):
        supply = self.get_object()
        if supply.status != Supply.PENDING_APPROVAL:
            return Response({"detail": "Нельзя reject не из pending_approval"}, status=400)
        
        ser = DecisionSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        
        if hasattr(supply, "decision_comment"):
            supply.decision_comment = ser.validated_data.get("decision_comment", "")
            
        supply.status = Supply.REJECTED
        supply.save()
        return Response(status=200)
    
    
    @extend_schema(summary="Закрыть (approved/rejected -> closed)", request=None, responses={200: None})
    @action(detail=True, methods=["post"], url_path="close",
            permission_classes=[HasCommodityExpertGroupPermission | HasMainOfficeGroupPermission])
    def close(self, request, pk=None):
        supply = self.get_object()
        if supply.status not in (Supply.APPROVED, Supply.REJECTED):
            return Response({"detail": "Нельзя закрыть не из approved/rejected"}, status=400)
        supply.status = Supply.CLOSED
        supply.save(update_fields=["status"])
        return Response(status=200)
    
    
# ---------- SUPPLY PRODUCTS (строки поставки) ----------
    
@extend_schema_view(
    list=extend_schema(
        summary="Список продуктов в поставках",
        tags=[APISchemaTags.SUPPLIES],
        parameters=[
            OpenApiParameter(name="supply", required=False, type=int, description="Фильтр по supply_id"),
            OpenApiParameter(name="product", required=False, type=int, description="Фильтр по product_id"),
            OpenApiParameter(name="status", required=False, type=str, description="Фильтр по status"),
            OpenApiParameter(name="requires_review", required=False, type=str, description="true/false/1/0"),
        ],
    ),
    retrieve=extend_schema(summary="Детали продукта в поставке", tags=[APISchemaTags.SUPPLIES]),
    create=extend_schema(summary="Создать продукт в поставке", tags=[APISchemaTags.SUPPLIES]),
    update=extend_schema(summary="Обновить продукт в поставке", tags=[APISchemaTags.SUPPLIES]),
    partial_update=extend_schema(summary="Частично обновить продукт в поставке", tags=[APISchemaTags.SUPPLIES]),
    destroy=extend_schema(summary="Удалить продукт в поставке", tags=[APISchemaTags.SUPPLIES]),
)
class SupplyProductViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    queryset = SupplyProduct.objects.all()
    serializer_class = SupplyProductRequestSerializer
    lookup_field = "id"
    
    def get_queryset(self):
        qs = super().get_queryset()
        p = self.request.query_params
        
        if p.get("supply"):
            qs = qs.filter(supply_id=p["supply"])
        if p.get("product"):
            qs = qs.filter(product_id=p["product"])
        if p.get("status"):
            qs = qs.filter(status=p["status"])
            
        b = _as_bool(p.get("requires_review"))
        if b is not None:
            qs = qs.filter(requires_review=b)
            
        return qs
    
    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated, HasSuppliesWorkflowWritePermission]
        return [p() for p in permission_classes]
    
    
# ---------- SUPPLY PRODUCT LOTS (партии факт) ----------
    
@extend_schema_view(
    list=extend_schema(
        summary="Список партий (факт)",
        tags=[APISchemaTags.SUPPLIES],
        parameters=[
            OpenApiParameter(name="supply", required=False, type=int, description="Фильтр по supply_id"),
            OpenApiParameter(name="supply_product", required=False, type=int, description="Фильтр по supply_product_id"),
            OpenApiParameter(name="status", required=False, type=str, description="Фильтр по status"),
            OpenApiParameter(name="packaging_condition", required=False, type=str, description="ok/damaged"),
            OpenApiParameter(name="expiry_from", required=False, type=str, description="expiry_date_actual >= YYYY-MM-DD"),
            OpenApiParameter(name="expiry_to", required=False, type=str, description="expiry_date_actual <= YYYY-MM-DD"),
        ],
    ),
    retrieve=extend_schema(summary="Детали партии (факт)", tags=[APISchemaTags.SUPPLIES]),
    create=extend_schema(summary="Создать партию (факт)", tags=[APISchemaTags.SUPPLIES]),
    update=extend_schema(summary="Обновить партию (факт)", tags=[APISchemaTags.SUPPLIES]),
    partial_update=extend_schema(summary="Частично обновить партию (факт)", tags=[APISchemaTags.SUPPLIES]),
    destroy=extend_schema(summary="Удалить партию (факт)", tags=[APISchemaTags.SUPPLIES]),
)
class SupplyProductLotViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    queryset = SupplyProductLot.objects.all()
    serializer_class = SupplyProductLotRequestSerializer
    lookup_field = "id"
    
    def get_queryset(self):
        qs = super().get_queryset()
        p = self.request.query_params
        
        if p.get("supply_product"):
            qs = qs.filter(supply_product_id=p["supply_product"])
        if p.get("supply"):
            qs = qs.filter(supply_product__supply_id=p["supply"])
        if p.get("status"):
            qs = qs.filter(status=p["status"])
        if p.get("packaging_condition"):
            qs = qs.filter(packaging_condition=p["packaging_condition"])
            
        if p.get("expiry_from"):
            qs = qs.filter(expiry_date_actual__gte=p["expiry_from"])
        if p.get("expiry_to"):
            qs = qs.filter(expiry_date_actual__lte=p["expiry_to"])
            
        return qs
    
    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated, HasSuppliesWorkflowWritePermission]
        return [p() for p in permission_classes]
    
    
# ---------- DISCREPANCY REASONS ----------
    
@extend_schema_view(
    list=extend_schema(summary="Список причин несоответствий", tags=[APISchemaTags.SUPPLIES]),
    retrieve=extend_schema(summary="Детали причины", tags=[APISchemaTags.SUPPLIES]),
    create=extend_schema(summary="Создать причину", tags=[APISchemaTags.SUPPLIES]),
    update=extend_schema(summary="Обновить причину", tags=[APISchemaTags.SUPPLIES]),
    partial_update=extend_schema(summary="Частично обновить причину", tags=[APISchemaTags.SUPPLIES]),
    destroy=extend_schema(summary="Удалить причину", tags=[APISchemaTags.SUPPLIES]),
)
class DiscrepancyReasonViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    queryset = DiscrepancyReason.objects.all()
    serializer_class = DiscrepancyReasonRequestSerializer
    lookup_field = "id"
    
    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated, HasSuppliesWorkflowWritePermission]
        return [p() for p in permission_classes]
    
    
# ---------- DISCREPANCIES ----------
    
@extend_schema_view(
    list=extend_schema(
        summary="Список несоответствий",
        tags=[APISchemaTags.SUPPLIES],
        parameters=[
            OpenApiParameter(name="status", required=False, type=str, description="Фильтр по status"),
            OpenApiParameter(name="reason", required=False, type=int, description="Фильтр по discrepancy_reason_id"),
            OpenApiParameter(name="created_by", required=False, type=int, description="created_by (employee_id)"),
            OpenApiParameter(name="decided_by", required=False, type=int, description="decided_by (employee_id)"),
            OpenApiParameter(name="supply", required=False, type=int, description="Фильтр по supply_id"),
            OpenApiParameter(name="supply_product", required=False, type=int, description="Фильтр по supply_product_id"),
            OpenApiParameter(name="lot", required=False, type=int, description="Фильтр по supply_product_lot_id"),
        ],
    ),
    retrieve=extend_schema(summary="Детали несоответствия", tags=[APISchemaTags.SUPPLIES]),
    create=extend_schema(summary="Создать несоответствие", tags=[APISchemaTags.SUPPLIES]),
    update=extend_schema(summary="Обновить несоответствие", tags=[APISchemaTags.SUPPLIES]),
    partial_update=extend_schema(summary="Частично обновить несоответствие", tags=[APISchemaTags.SUPPLIES]),
    destroy=extend_schema(summary="Удалить несоответствие", tags=[APISchemaTags.SUPPLIES]),
)
class SupplyDiscrepancyViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    queryset = SupplyDiscrepancy.objects.all()
    serializer_class = SupplyDiscrepancyRequestSerializer
    lookup_field = "id"
    
    def get_queryset(self):
        qs = super().get_queryset()
        p = self.request.query_params
        
        if p.get("status"):
            qs = qs.filter(status=p["status"])
        if p.get("reason"):
            qs = qs.filter(discrepancy_reason_id=p["reason"])
        if p.get("created_by"):
            qs = qs.filter(created_by_id=p["created_by"])
        if p.get("decided_by"):
            qs = qs.filter(decided_by_id=p["decided_by"])
            
        if p.get("lot"):
            qs = qs.filter(supply_product_lot_id=p["lot"])
        if p.get("supply_product"):
            qs = qs.filter(supply_product_lot__supply_product_id=p["supply_product"])
        if p.get("supply"):
            qs = qs.filter(supply_product_lot__supply_product__supply_id=p["supply"])
            
        return qs
    
    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated, HasSuppliesWorkflowWritePermission]
        return [p() for p in permission_classes]
    
    @extend_schema(summary="Отправить в ГК (open -> sent_to_hq)", request=None, responses={200: None})
    @action(detail=True, methods=["post"], url_path="send-to-hq",
            permission_classes=[HasCommodityExpertGroupPermission])
    def send_to_hq(self, request, pk=None):
        d = self.get_object()
        if d.status != SupplyDiscrepancy.OPEN:
            return Response({"detail": "Можно отправить только из open"}, status=400)
        d.status = SupplyDiscrepancy.SENT_TO_HQ
        d.save(update_fields=["status"])
        return Response(status=200)
    
    
    @extend_schema(summary="ГК: одобрить (sent_to_hq -> approved)", request=DecisionSerializer, responses={200: None})
    @action(detail=True, methods=["post"], url_path="approve",
            permission_classes=[HasMainOfficeGroupPermission])
    def approve(self, request, pk=None):
        d = self.get_object()
        if d.status != SupplyDiscrepancy.SENT_TO_HQ:
            return Response({"detail": "Можно approve только из sent_to_hq"}, status=400)
        ser = DecisionSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        set_discrepancy_decision(d, request.user, SupplyDiscrepancy.APPROVED, ser.validated_data.get("decision_comment", ""))
        return Response(status=200)
    
    
    @extend_schema(summary="ГК: отклонить (sent_to_hq -> rejected)", request=DecisionSerializer, responses={200: None})
    @action(detail=True, methods=["post"], url_path="reject",
            permission_classes=[HasMainOfficeGroupPermission])
    def reject(self, request, pk=None):
        d = self.get_object()
        if d.status != SupplyDiscrepancy.SENT_TO_HQ:
            return Response({"detail": "Можно reject только из sent_to_hq"}, status=400)
        ser = DecisionSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        set_discrepancy_decision(d, request.user, SupplyDiscrepancy.REJECTED, ser.validated_data.get("decision_comment", ""))
        return Response(status=200)
    
    
    @extend_schema(summary="Урегулировать (approved/rejected -> resolved)", request=DecisionSerializer, responses={200: None})
    @action(detail=True, methods=["post"], url_path="resolve",
            permission_classes=[HasCommodityExpertGroupPermission | HasMainOfficeGroupPermission])
    def resolve(self, request, pk=None):
        d = self.get_object()
        if d.status not in (SupplyDiscrepancy.APPROVED, SupplyDiscrepancy.REJECTED):
            return Response({"detail": "Можно resolve только из approved/rejected"}, status=400)
        ser = DecisionSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        set_discrepancy_decision(d, request.user, SupplyDiscrepancy.RESOLVED, ser.validated_data.get("decision_comment", ""))
        return Response(status=200)
    
    
# ---------- DISCREPANCY ATTACHMENTS (multipart) ----------
    
@extend_schema_view(
    list=extend_schema(
        summary="Список вложений",
        tags=[APISchemaTags.SUPPLIES],
        parameters=[
            OpenApiParameter(name="discrepancy", required=False, type=int, description="Фильтр по supply_discrepancy_id"),
        ],
    ),
    retrieve=extend_schema(summary="Детали вложения", tags=[APISchemaTags.SUPPLIES]),
    create=extend_schema(summary="Загрузить вложение", tags=[APISchemaTags.SUPPLIES]),
    destroy=extend_schema(summary="Удалить вложение", tags=[APISchemaTags.SUPPLIES]),
)
class DiscrepancyAttachmentViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    queryset = DiscrepancyAttachment.objects.all()
    serializer_class = DiscrepancyAttachmentRequestSerializer
    lookup_field = "id"
    parser_classes = [MultiPartParser, FormParser]
    
    def get_queryset(self):
        qs = super().get_queryset()
        p = self.request.query_params
        
        if p.get("discrepancy"):
            qs = qs.filter(supply_discrepancy_id=p["discrepancy"])
            
        return qs
    
    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated, HasSuppliesWorkflowWritePermission]
        return [p() for p in permission_classes]