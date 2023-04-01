from django.conf import settings
from rest_framework import permissions


class CurrentUserOrSuperuserOrReadOnly(permissions.BasePermission):
    """Права доступа для авторизированного пользователя либо администратора.
    Пермишен используется для доступа к персональным страницам."""
    def has_permission(self, request, view):
        return ((request.path_info == settings.USER_ME_PATH
             and request.user.is_authenticated) or
             (request.path_info != settings.USER_ME_PATH
              and request.method in permissions.SAFE_METHODS
              or request.user.is_superuser
              or request.user.is_staff))


class IsAdminAuthorOrReadOnly(permissions.BasePermission):
    """Права доступа для автора либо алминистратора."""
    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated)
    
    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_superuser
                or request.user.is_staff
                or obj.author == request.user)
