from rest_framework import serializers

from .models import Shop, Category, Product


class RecursiveField(serializers.Serializer):
    '''сериализатор для рекурсивного вывода вложенных данных'''
    def to_representation(self, instance):
        serializer = self.parent.parent.__class__(instance, context=self.context)
        return serializer.data


class ProductSerializer(serializers.ModelSerializer):
    shop = serializers.SlugRelatedField(slug_field='name', read_only=True)
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)


    class Meta:
        model = Product
        fields = ['id', 'category', 'shop', 'name', 'model', 'quantity', 'price_rrc']


class CategorySerializer(serializers.ModelSerializer):
    # shop = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    # products = RecursiveField(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name']


class ShopCreteSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Shop
        fields = '__all__'


class ShopDetailSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='email', read_only=True)
    categories = CategorySerializer(read_only=True, many=True)
    # categories = RecursiveField(read_only=True, many=True)
    products_info = ProductSerializer(read_only=True, many=True)

    class Meta:
        model = Shop
        fields = ['id', 'name', 'url', 'state', 'user', 'categories', 'products_info']


class ShopsListSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='email', read_only=True)

    class Meta:
        model = Shop
        fields = ['id', 'name', 'state', 'url', 'user']


