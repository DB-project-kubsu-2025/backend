from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from shops.models import ProductMedia


def generate_file_path(instance: 'ProductMedia', filename: str):
    """Сгенерировать путь к файлу"""
    return f'product_media/{instance.id}/{filename}'
