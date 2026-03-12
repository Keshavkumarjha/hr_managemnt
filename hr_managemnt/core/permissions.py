from rest_framework.permissions import BasePermission


class IsHRAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in {"GET", "HEAD", "OPTIONS"}:
            return bool(request.user and request.user.is_authenticated)
        return bool(
            request.user
            and request.user.is_authenticated
            and (request.user.is_staff or request.user.groups.filter(name="HR_ADMIN").exists())
        )
