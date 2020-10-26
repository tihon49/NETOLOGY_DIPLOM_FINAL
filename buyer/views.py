from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Order, ItemInOrder
from .serializers import OrderSerializer, OrderItemSerializer, OrderItemAddSerializer, OrderCreateSerializer


class OrderSerializerView(APIView):
    '''вывод заказа/корзины пользователя'''

    def get(self, request):
        user = request.user
        try:
            order = Order.objects.get(user=user, status='В корзине')
            serializer = OrderSerializer(order)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response({'response': f'Уважаемый {request.user}, Ваша корзина пока пуста.',
                             'help_info': 'Перейдите по ссылке http://127.0.0.1:8000/api/v1/cart/create/'})


class OrderCreateView(viewsets.ModelViewSet):
    '''создать заказ'''
    serializer_class = OrderCreateSerializer
    queryset = Order.objects.all()

    def get_queryset(self):
        order = Order.objects.filter(user=self.request.user, status='В корзине')
        return order


class AddItemInOrderView(generics.CreateAPIView):
    '''добавить товар в заказ'''
    serializer_class = OrderItemAddSerializer

    def get_queryset(self):
        order = Order.objects.filter(user=self.request.user, status='В корзине')
        return order


class ItemsInOrderView(viewsets.ModelViewSet):
    '''вывод заказанных товаров из заказа/корзины'''
    serializer_class = OrderItemSerializer
    queryset = ItemInOrder.objects.all()

    def get_queryset(self):
        order = Order.objects.filter(user=self.request.user, status='В корзине').first()
        items = ItemInOrder.objects.filter(order=order)
        return items


class CartConfirmView(APIView):
    def get(self, request):
        user = request.user
        try:
            order = Order.objects.get(user=user, status='В корзине')
            order.status = 'Подтвержден'
            order.is_active = True
            order.save()
            return Response({'response': 'Ваш заказ подтвержден.'})
        except ObjectDoesNotExist:
            return Response({'response': f'Уважаемый {request.user}, Ваша корзина пока пуста.',
                             'help_info': 'Перейдите по ссылке http://127.0.0.1:8000/api/v1/cart/create/'})