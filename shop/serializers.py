from rest_framework import serializers

from .models import Shop, Category, Product, Parameter, ProductParameter


# class RecursiveField(serializers.Serializer):
#     '''сериализатор для рекурсивного вывода вложенных данных'''
#     def to_representation(self, instance):
#         serializer = self.parent.parent.__class__(instance, context=self.context)
#         return serializer.data


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class ProductParameterSerializer(serializers.ModelSerializer):
    parameter = serializers.StringRelatedField()

    class Meta:
        model = ProductParameter
        fields = ['parameter', 'value']


class ProductSerializer(serializers.ModelSerializer):
    shop = serializers.StringRelatedField()
    category = serializers.StringRelatedField()
    product_info_parameters = ProductParameterSerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields = ('id', 'shop', 'name', 'category', 'external_id', 'model', 'quantity',
                  'price', 'price_rrc', 'product_info_parameters')


class ShopCreteSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Shop
        fields = '__all__'


class ShopDetailSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='email', read_only=True)
    # categories = CategorySerializer(read_only=True, many=True)
    # categories = RecursiveField(read_only=True, many=True)
    # products_info = ProductSerializer(read_only=True, many=True)

    class Meta:
        model = Shop
        fields = ['id', 'name', 'url', 'user']


class ShopsListSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='email', read_only=True)

    class Meta:
        model = Shop
        fields = ['id', 'name', 'state', 'url', 'user']