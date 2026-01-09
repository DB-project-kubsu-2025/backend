from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

User = get_user_model()


def get_user_groups(user_id: int) -> dict[str, list[str]]:
    """
    Хук для получения групп пользователя.

    :param user_id: ID пользователя
    :return: { "<user_id>": ["group1", "group2"] }
    """
    user = (
        User.objects
        .prefetch_related('groups')
        .filter(id=user_id)
        .first()
    )

    if not user:
        return {str(user_id): []}

    groups = list(user.groups.values_list('name', flat=True))

    return {
        str(user_id): groups
    }
