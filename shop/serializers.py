from rest_framework import serializers

from shop.models import Shop, Category, Product, ProductInfo



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name']

class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)
    class Meta:
        model = Category
        fields = ['id', 'name', 'products']


class ProductInfoSerializer(serializers.ModelSerializer):
    product = ProductSerializer
    class Meta:
        model = ProductInfo
        fields = ['product', 'id', 'model', 'external_id', 'quantity', 'price']


class ShopsListSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='email', read_only=True)
    # categories = CategorySerializer(many=True)
    product_infos = ProductInfoSerializer(many=True)

    class Meta:
        model = Shop
        fields = ['id', 'name', 'state', 'url', 'user', 'product_infos']


class ShopCreteSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Shop
        fields = '__all__'


class ShopDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # user = serializers.SlugRelatedField(slug_field='email', read_only=True)
    category = ShopCreteSerializer

    class Meta:
        model = Shop
        fields = '__all__'