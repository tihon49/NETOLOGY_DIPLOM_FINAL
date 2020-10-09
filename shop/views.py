from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q

from shop.models import Shop, Category, Product
from shop.serializers import (ShopDetailSerializer, ShopCreteSerializer,
                              ShopsListSerializer, CategorySerializer, ProductSerializer)
from rest_framework.permissions import IsAdminUser, IsAuthenticated


class ShopCreateView(generics.CreateAPIView):
    serializer_class = ShopCreteSerializer
    permission_classes = (IsAuthenticated,)


class ShopsListView(generics.ListAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopsListSerializer
    # permission_classes = (IsAdminUser,)


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


class ProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    pagination_class = PageNumberPagination


# class ProductView(APIView):
#     def get(self, request, *args, **kwargs):
#         query = Q(shop__state=True)
#         shop_id = request.query_params.get('shop_id')
#         category_id = request.query_params.get('category_id')
#
#         if shop_id:
#             query = query & Q(shop_id=shop_id)
#             print(query)
#
#         if category_id:
#             query = query & Q(category_id=category_id)
#
#         queryset = Product.objects.filter(query).select_related(
#             'shop', 'category').prefetch_related(
#             'product_info_parameters').distinct()
#         serializer = ProductSerializer(queryset, many=True)
#         return Response(serializer.data)
