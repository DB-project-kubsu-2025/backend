from dataclasses import dataclass


@dataclass
class HistoricalDataItem:
    """Единица исторических данных"""

    date: str
    sales: int


@dataclass
class HistoricalData:
    """Исторические данные"""

    historical_data_items: list[HistoricalDataItem]
