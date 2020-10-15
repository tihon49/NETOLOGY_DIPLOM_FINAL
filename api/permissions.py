from rest_framework import permissions


class IsShop(permissions.BasePermission):
    message = 'You must be a Shop type user.'

    def has_permission(self, request, view):
        return request.user.type == 'shop'


class IsShopOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # if request.method in permissions.SAFE_METHODS:
        #     return True
        return obj.user == request.user
