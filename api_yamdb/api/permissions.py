from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or (request.user.is_authenticated
                    and (request.user.is_admin
                         or request.user.is_superuser
                         or request.user.is_staff)))

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or (request.user.is_authenticated
                    and (request.user.is_admin
                         or request.user.is_superuser
                         or request.user.is_staff)))


class IsAdministrator(permissions.BasePermission):
    def has_permission(self, request, view):
        return ((request.user.is_admin or request.user.is_superuser)
                and request.user.is_authenticated)


class IsAnAuthor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or request.user in obj.authors)


class IsAuthorOrModerator(permissions.BasePermission):
    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        user = request.user
        return (request.method in permissions.SAFE_METHODS
                or (user.is_authenticated
                    and (obj.author == user or user.is_moderator
                         or user.is_admin)))
