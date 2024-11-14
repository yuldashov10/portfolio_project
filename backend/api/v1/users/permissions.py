from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsOwnerOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj) -> bool:
        return obj.user == request.user or request.user.is_admin


class IsOwnerOrReadOnly(BasePermission):
    def has_permission(self, request, view) -> bool:
        return request.method in SAFE_METHODS or request.user.is_authenticated

    def has_object_permission(self, request, view, obj) -> bool:
        return (
            request.method in SAFE_METHODS
            or request.user.is_authenticated
            and obj.user == request.user
        )
