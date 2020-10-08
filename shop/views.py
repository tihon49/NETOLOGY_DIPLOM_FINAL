from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from shop.models import Shop, Category
from shop.serializers import ShopDetailSerializer, ShopCreteSerializer, ShopsListSerializer, CategorySerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated


class ShopCreateView(generics.CreateAPIView):
    serializer_class = ShopCreteSerializer
    permission_classes = (IsAuthenticated,)


class ShopsListView(generics.ListAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopsListSerializer
#     permission_classes = (IsAdminUser,)


class ShopDetailView(APIView):
    def get(self, request, *args, **kwargs):
        shop = request.user.shop
        serializer = ShopDetailSerializer(shop)
        return Response(serializer.data)

    def put(self, request):
        shop = request.user.shop
        serializer = ShopDetailSerializer(shop, request.data)

        data = {}
        if serializer.is_valid():
            serializer.save()
            data['request'] = f'Shop {shop} successfully updated'
        else:
            raise serializer.errors
        return Response(data)

    def delete(self, request):
        shop = request.user.shop
        shop.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# https://www.youtube.com/watch?v=C6S3dMt1s_M&t=5074s   at 1:24:55
# class ShopUpdateView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = ShopDetailSerializer
#     queryset = Shop.objects.all()
#     permission_classes = (IsShopOwnerOrReadOnly,)


class CategoryListView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()