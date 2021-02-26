from rest_framework import permissions


class IsCurrentUserOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            '''
            The method is a safe mood
            '''
            return True
        else:
            '''
            The method is not a safe method
            Only owner are granted permissions for unsafe methods
            '''
            return obj.owner == request.user
