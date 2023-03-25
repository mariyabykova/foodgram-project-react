from rest_framework import permissions


class CurrentUserOrSuperuserOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return ((request.path_info == '/api/users/me/'
             and request.user.is_authenticated) or
             (request.path_info != '/api/users/me/'
              and request.method in permissions.SAFE_METHODS
              or request.user.is_superuser))
