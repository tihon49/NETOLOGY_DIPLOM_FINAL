from rest_framework import serializers

from accounts.serializers import ContactSerializer
from shop.models import Product
from .models import Order, ItemInOrder


class ProductSerializer(serializers.ModelSerializer):
    shop = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = ['name', 'model', 'shop']


class OrderItemSerializer(serializers.ModelSerializer):
    # shop = serializers.StringRelatedField()
    category = serializers.StringRelatedField()
    product_name = ProductSerializer(read_only=True)

    class Meta:
        model = ItemInOrder
        fields = ['id', 'external_id', 'category', 'product_name', 'quantity',
                  'price_per_item', 'total_price']
        read_only_fields = ['id', 'price_per_item', 'total_price']


class OrderItemAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemInOrder
        fields = ['external_id', 'category', 'product_name', 'quantity', 'order']


class OrderCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ['status', 'contact', 'total_price', 'total_items_count']


class OrderUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'status', 'contact']
        read_only_fields = ['id']


class OrderSerializer(serializers.ModelSerializer):
    ordered_items = OrderItemSerializer(read_only=True, many=True)
    total_price = serializers.IntegerField()
    total_items_count = serializers.IntegerField()
    contact = ContactSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'status', 'total_items_count',
                  'total_price', 'contact', 'ordered_items')
        read_only_fields = ('id',)
