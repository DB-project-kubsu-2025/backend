from django.db.models import Sum
from django.db.models.functions import TruncDate

from ml_service.types import HistoricalData, HistoricalDataItem
from shops.models import SalesReceiptLine, SaleReceipt


def get_data_for_prediction(product_category: str) -> HistoricalData:
    """Получить данные для прогнозирования"""
    daily_sales = (
        SalesReceiptLine.objects.select_related(
            'sale_receipt__storage',
            'sale_receipt__cashier',
            'inventory_lot__product__category',
            'price_list_type',
            'price_list_base',
            'coupon',
        ).filter(
            sale_receipt__status=SaleReceipt.PAID,
            inventory_lot__product__category__ml_service_category=product_category,
        )
        .annotate(date_only=TruncDate('sale_receipt__closed_at'), sales=Sum('quantity'))
        .values('date_only', 'sales')
        .order_by('date_only')
    )

    return HistoricalData(
        historical_data_items=[
            HistoricalDataItem(date=sale['date_only'].strftime("%Y-%m-%d"), sales=sale['sales'])
            for sale in daily_sales
            if sale['date_only'] is not None
        ],
    )
