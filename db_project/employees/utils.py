from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from employees.models import LeaveRequestAttachment


def generate_file_path(instance: 'LeaveRequestAttachment', filename: str):
    """Сгенерировать путь к файлу"""
    return f'attachments/{instance.id}/{filename}'
