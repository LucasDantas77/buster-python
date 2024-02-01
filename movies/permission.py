from rest_framework import permissions
from rest_framework.views import Request, View


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request: Request, view: View):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
            and request.user.is_superuser
        )


class IsAdminAcess(IsAdmin):
    def has_permission(self, request: Request, view: View):
        if request.method == "GET":
            return True
        return super().has_permission(request, view)
