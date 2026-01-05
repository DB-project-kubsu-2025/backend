from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from shops.models import ProductMedia, WriteoffAttachment


def generate_file_path(instance: 'ProductMedia', filename: str):
    """Сгенерировать путь к файлу"""
    return f'product_media/{instance.id}/{filename}'


def generate_file_path_for_writeoff(instance: 'ProductMedia', filename: str):
    """Сгенерировать путь к файлу"""
    return f'product_media/{instance.id}/{filename}'
