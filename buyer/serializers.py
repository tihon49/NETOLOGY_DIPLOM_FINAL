from rest_framework import serializers

from accounts.serializers import ContactSerializer
from shop.models import Product
from .models import Order, ItemInOrder


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name']


class OrderItemSerializer(serializers.ModelSerializer):
    shop = serializers.StringRelatedField()
    category = serializers.StringRelatedField()
    product_name = ProductSerializer(read_only=True)

    class Meta:
        model = ItemInOrder
        fields = ['id', 'external_id', 'category', 'shop', 'product_name', 'quantity',
                  'price_per_item', 'total_price']
        read_only_fields = ['id', 'external_id', 'price_per_item', 'total_price']


class OrderItemAddSerializer(serializers.ModelSerializer):
    # product_name = serializers.StringRelatedField()

    class Meta:
        model = ItemInOrder
        fields = ['external_id', 'product_name', 'quantity', 'price_per_item',
                  'total_price', 'category', 'shop', 'order']
        read_only_fields = ['price_per_item', 'total_price']


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
