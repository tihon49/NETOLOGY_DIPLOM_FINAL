from pprint import pprint

from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination

from api.permissions import IsShopOwnerOrReadOnly, IsShop
from buyer.models import ItemInOrder, Order
from shop.models import Shop, Category, Product
from shop.serializers import (ShopDetailSerializer, ShopCreteSerializer,
                              ShopsListSerializer, CategorySerializer, ProductSerializer, ShopBaseSerializer,
                              ShopOrderSerializer)
from rest_framework.permissions import IsAdminUser, IsAuthenticated


class ShopCreateView(generics.CreateAPIView):
    '''создание магазина'''
    serializer_class = ShopCreteSerializer
    permission_classes = (IsAuthenticated, IsShop)


class ShopsListView(generics.ListAPIView):
    '''представление всех магазинов'''
    queryset = Shop.objects.all()
    serializer_class = ShopsListSerializer
    # permission_classes = (IsAdminUser,)


class ShopDetailView(viewsets.ModelViewSet):
    '''детальное представление магазина'''
    serializer_class = ShopDetailSerializer

    def get_queryset(self):
        shop = Shop.objects.filter(user=self.request.user)
        return shop


class ShopBaseView(APIView):
    '''
    базовое представление магазина с возможностью редактирования и удаления
    '''

    def get(self, request, *args, **kwargs):
        try:
            shop = request.user.shop
            serializer = ShopBaseSerializer(shop)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response({'response': 'Shop does not exist'})

    def put(self, request):
        shop = request.user.shop
        serializer = ShopBaseSerializer(shop, request.data)

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
# тут у меня не заработало как надо....


class CategoryListView(generics.ListAPIView):
    '''все категории'''
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class ProductListView(generics.ListAPIView):
    '''все товары'''
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    pagination_class = PageNumberPagination


class ShopOrdersView(viewsets.ModelViewSet):
    serializer_class = ShopOrderSerializer
    queryset = ItemInOrder.objects.all()

    def get_queryset(self):
        shop_owner = self.request.user
        shop = Shop.objects.get(user=shop_owner)
        items = ItemInOrder.objects.filter(shop=shop, order__is_active=True)
        return items

