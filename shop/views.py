from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from api.permissions import IsOwnerOrReadOnly, IsShopOwnerOrReadOnly
from shop.models import Shop
from shop.serializers import ShopsListSerializer, ShopDetailSerializer, ShopCreteSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated


class ShopCreateView(generics.CreateAPIView):
    serializer_class = ShopDetailSerializer
    permission_classes = (IsAuthenticated, )


class ShopsListView(generics.ListAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopsListSerializer
    permission_classes = (IsAdminUser,)


class ShopDetailView(APIView):
    def get(self, request):
        user = request.user
        shop = Shop.objects.get(user = user)
        serializer = ShopDetailSerializer(shop)
        return Response(serializer.data)


#https://www.youtube.com/watch?v=C6S3dMt1s_M&t=5074s   at 1:24:55
class ShopUpdateView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ShopDetailSerializer
    queryset = Shop.objects.all()
    permission_classes = (IsShopOwnerOrReadOnly,)


# class ShopDetailView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = ShopDetailSerializer
#
#     def get_queryset(self):
#         user = self.request.user
#         return user
#
#     def get(self):
#         user = self.request.user
#         shop = Shop.objects.get(user = user)
#         serializer = ShopDetailSerializer(shop)
#         return Response(serializer.data)


