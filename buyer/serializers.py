from rest_framework import serializers

from accounts.serializers import ContactSerializer
from .models import Order, ItemInOrder


class OrderItemSerializer(serializers.ModelSerializer):
    shop = serializers.StringRelatedField()
    category = serializers.StringRelatedField()

    class Meta:
        model = ItemInOrder
        fields = ['id', 'product_name', 'external_id', 'quantity',
                  'price_per_item', 'total_price', 'order', 'category', 'shop']
        read_only_fields = ['id']
        extra_kwargs = {'order': {'write_only': True}}


class OrderItemAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemInOrder
        fields = ['product_name', 'external_id', 'quantity', 'price_per_item',
                  'total_price', 'order', 'category', 'shop']


class OrderUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'status', 'contact']
        read_only_fields = ['id']


class OrderSerializer(serializers.ModelSerializer):
    ordered_items = OrderItemSerializer(read_only=True, many=True)

    total_sum = serializers.IntegerField()
    total_quantity = serializers.IntegerField()
    contact = ContactSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'status', 'total_items_count',
                  'total_price', 'contact', 'ordered_items')
        read_only_fields = ('id',)
