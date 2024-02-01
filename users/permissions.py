from rest_framework.permissions import BasePermission, IsAuthenticated


class UserAuthenticate(IsAuthenticated, BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated


class UserAuth(BasePermission):
    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False
        if request.user.is_employee:
            return True
        if obj == request.user:
            return True
        return False
