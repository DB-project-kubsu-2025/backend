from rest_framework import permissions


class HasDirectorGroupPermission(permissions.BasePermission):
    """Пользователь принадлежит группе director_group"""

    def has_permission(self, request, view):
        """Проверить наличие разрешения"""
        return request.user.groups.filter(name='director_group').exists()


class HasMainOfficeGroupPermission(permissions.BasePermission):
    """Пользователь принадлежит группе main_office_group"""

    def has_permission(self, request, view):
        """Проверить наличие разрешения"""
        return request.user.groups.filter(name='main_office_group').exists()


class HasStorageGroupPermission(permissions.BasePermission):
    """Пользователь принадлежит группе storage_group"""

    def has_permission(self, request, view):
        """Проверить наличие разрешения"""
        return request.user.groups.filter(name='storage_group').exists()


class HasCommodityExpertGroupPermission(permissions.BasePermission):
    """Пользователь принадлежит группе commodity_expert_group"""

    def has_permission(self, request, view):
        return request.user.groups.filter(name='commodity_expert_group').exists()


class HasStorekeeperGroupPermission(permissions.BasePermission):
    """Пользователь принадлежит группе storekeeper_group"""

    def has_permission(self, request, view):
        return request.user.groups.filter(name='storekeeper_group').exists()


class HasSellerGroupPermission(permissions.BasePermission):
    """Пользователь принадлежит группе seller_group"""

    def has_permission(self, request, view):
        return request.user.groups.filter(name='seller_group').exists()
