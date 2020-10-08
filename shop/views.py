from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.permissions import IsShopOwnerOrReadOnly, IsShop
from shop.models import Shop #Category
from shop.serializers import ShopDetailSerializer, ShopCreteSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated


class ShopCreateView(generics.CreateAPIView):
    serializer_class = ShopCreteSerializer
    permission_classes = (IsAuthenticated, IsShop)


# class ShopsListView(generics.ListAPIView):
#     queryset = Shop.objects.all()
#     serializer_class = ShopsListSerializer
#     permission_classes = (IsAdminUser,)


class ShopDetailView(APIView):
    def get(self, request, *args, **kwargs):
        print(request.user)
        shop = request.user.shop
        serializer = ShopDetailSerializer(shop)
        return Response(serializer.data)


# https://www.youtube.com/watch?v=C6S3dMt1s_M&t=5074s   at 1:24:55
class ShopUpdateView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ShopDetailSerializer
    queryset = Shop.objects.all()
    permission_classes = (IsShopOwnerOrReadOnly,)


# class CategoryView(generics.ListAPIView):
#     serializer_class = CategorySerializer
#     queryset = Category.objects.all()