from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from api.permissions import IsOwnerOrReadOnly
from shop.models import Shop
from shop.serializers import ShopsListSerializer, ShopDetailSerializer
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


class ShopDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ShopDetailSerializer

    def get_queryset(self):
        user = self.request.user

    def get(self):
        user = self.request.user
        shop = Shop.objects.get(user = user)
        serializer = ShopDetailSerializer(shop)
        return Response(serializer.data)


