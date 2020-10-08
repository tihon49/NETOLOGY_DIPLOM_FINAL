from rest_framework import serializers

from .models import Shop, Category


# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = ['name']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


# class ProductInfoSerializer(serializers.ModelSerializer):
#     product = ProductSerializer
#
#     class Meta:
#         model = ProductInfo
#         fields = ['product', 'id', 'model', 'external_id', 'quantity', 'price']


class ShopCreteSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Shop
        fields = '__all__'


class ShopDetailSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='email', read_only=True)

    class Meta:
        model = Shop
        fields = ['id', 'name', 'url', 'state', 'user']


class ShopsListSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='email', read_only=True)
    # categories = CategorySerializer(many=True)
    # product_infos = ProductInfoSerializer(many=True)

    class Meta:
        model = Shop
        fields = ['id', 'name', 'state', 'url', 'user']
