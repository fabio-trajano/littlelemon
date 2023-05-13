from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAdminUser


class ManagerPermission(BasePermission):
    def has_permission(self, request, view):
        return IsAdminUser().has_permission(request, view) or request.user.groups.filter(name='Manager').exists()


class DeliveryCrewPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Delivery Crew').exists()


class ReadOnlyPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.method in SAFE_METHODS


class CustomerPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.count() == 0 or request.user.groups.filter(name='Customer').exists()
