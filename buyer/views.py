from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from buyer.models import Order, ItemInOrder
from buyer.serializers import OrderSerializer, OrderItemSerializer, OrderItemAddSerializer


class OrderSerializerView(APIView):
    '''вывод заказа/корзины пользователя'''
    def get(self, request):
        user = request.user
        try:
            order = Order.objects.get(user=user)
            serializer = OrderSerializer(order)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response({f'Уважаемый {request.user}, Ваша корзина пока пуста.'})


class AddItemInOrderView(generics.CreateAPIView):
    '''добавление товара в заказ'''
    serializer_class = OrderItemAddSerializer


class ItemsInOrderView(viewsets.ModelViewSet):
    '''вывод заказанных товаров из заказа/корзины'''
    serializer_class = OrderItemSerializer
    queryset = ItemInOrder.objects.all()

