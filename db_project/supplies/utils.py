from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from supplies.models import DiscrepancyAttachment


def generate_file_path(instance: 'DiscrepancyAttachment', filename: str):
    """Сгенерировать путь к файлу"""
    return f'discrepancy/{instance.id}/{filename}'
