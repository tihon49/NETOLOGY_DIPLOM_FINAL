from rest_framework import permissions


class IsShop(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # if request.method in permissions.SAFE_METHODS:
        #     return True
        return obj.user.type == 'shop'


class IsShopOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
