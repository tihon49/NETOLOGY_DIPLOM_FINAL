from pprint import pprint

from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination

from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from yaml import load as load_yaml, Loader
import requests

from api.permissions import IsShop
from buyer.models import ItemInOrder, Order
from shop.models import Shop, Category, Product, Parameter, ProductParameter, Brand
from shop.serializers import (ShopDetailSerializer, ShopCreteSerializer,
                              ShopsListSerializer, CategorySerializer, ProductSerializer, ShopBaseSerializer,
                              ShopOrderSerializer)
from rest_framework.permissions import IsAuthenticated


class ShopCreateView(generics.CreateAPIView):
    """создание магазина"""
    serializer_class = ShopCreteSerializer
    permission_classes = (IsAuthenticated, IsShop)


class ShopsListView(generics.ListAPIView):
    """представление всех магазинов"""
    queryset = Shop.objects.all()
    serializer_class = ShopsListSerializer
    # permission_classes = (IsAdminUser,)


class ShopDetailView(viewsets.ModelViewSet):
    """детальное представление магазина"""
    serializer_class = ShopDetailSerializer

    def get_queryset(self):
        shop = Shop.objects.filter(user=self.request.user)
        return shop


class ShopBaseView(APIView):
    """
    базовое представление магазина с возможностью редактирования и удаления
    """

    @staticmethod
    def get(request):
        try:
            shop = request.user.shop
            serializer = ShopBaseSerializer(shop)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response({'response': 'Shop does not exist'})

    @staticmethod
    def put(request):
        shop = request.user.shop
        serializer = ShopBaseSerializer(shop, request.data)

        data = {}
        if serializer.is_valid():
            serializer.save()
            data['request'] = f'Shop {shop} successfully updated'
        else:
            raise serializer.errors
        return Response(data)

    @staticmethod
    def delete(request):
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
    """все категории"""
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class ProductListView(generics.ListAPIView):
    """все товары"""
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    pagination_class = PageNumberPagination


class ShopOrdersView(viewsets.ModelViewSet):
    """получаем заказы магазина с возможностью изменения статуса заказа"""
    serializer_class = ShopOrderSerializer
    queryset = ItemInOrder.objects.all()

    def get_queryset(self):
        shop_owner = self.request.user
        shop = Shop.objects.get(user=shop_owner)
        order = Order.objects.filter(is_active=True, ordered_items__shop=shop)
        return order

class ShopUpdateView(APIView):
    """
    Импорт списка товаров из yaml
    """
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        if request.user.type != 'shop':
            return Response({'status': False, 'error': 'Только для магазинов'}, status=status.HTTP_403_FORBIDDEN)

        url = request.data.get('url')
        print(url)
        if url:
            validate_url = URLValidator()
            try:
                validate_url(url)
            except ValidationError as e:
                return Response({'status': False, 'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
            else:
                headers = {'Authorization': 'Token 94691a9e6afb4762cb97902d363bb69efc85c430'}
                stream = requests.get(url, headers=headers)

                data = load_yaml(stream.content, Loader=Loader)
                pprint(data)

                shop, _ = Shop.objects.get_or_create(user_id=request.user.id,
                                                     defaults={'name': data['name'], 'url': url})
                for category in data['categories']:
                    category_object, _ = Category.objects.get_or_create(id=category['id'], name=category['name'])
                    category_object.shops.add(shop.id)
                    category_object.save()

                for item in data['products_info']:
                    category_ = Category.objects.get(name=item['category'])
                    print(f'category: {category_}')
                    name_ = Brand.objects.get(name=item['name'])
                    print(f'name: {name_}')
                    product_ = Product.objects.create(
                        name= name_,
                        external_id=item['id'],
                        category=category_,
                        model=item['model'],
                        price=item['price'],
                        price_rrc=item['price_rrc'],
                        quantity=item['quantity'],
                        shop_id=shop.pk)
                    print(f'product: {product_}')
                    for name, value in item['product_info_parameters'].items():
                        print('\nhere\n')
                        parameter_id_, _ = Parameter.objects.get_or_create(name=name)
                        ProductParameter.objects.create(
                            product_id=product_.pk,
                            parameter_id=parameter_id_.pk,
                            value=value)

                if shop.name != data['name']:
                    return Response({'status': False, 'error': 'В файле указано некорректное название магазина!'},
                                    status=status.HTTP_400_BAD_REQUEST)

                return Response({'status': True})

        return Response({'status': False, 'error': 'Не указаны необходимые поля'},
                        status=status.HTTP_400_BAD_REQUEST)

# TODO: сделать так чтоб эта шляпа работала с файлом а не с урлом