from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user 


class IsSuperUserOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow only superusers to modify the data.
    """

    def has_permission(self, request, view):
        # Allow read-only access for any request
        if request.method in permissions.SAFE_METHODS:
            return True
        # Allow only superusers to make changes
        return request.user.is_superuser