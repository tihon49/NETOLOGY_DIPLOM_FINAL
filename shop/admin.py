from django.contrib import admin

from .models import Shop, Category, Product, Parameter, ProductParameter


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'url', 'user']
    list_display_links = ['id', 'name', 'url', 'user']


@admin.register(Category)
class ShopAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ShopAdmin(admin.ModelAdmin):
    list_display = ['name', 'model', 'external_id', 'shop', 'quantity', 'price', 'price_rrc']


@admin.register(Parameter)
class ShopAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductParameter)
class ShopAdmin(admin.ModelAdmin):
    list_display = ['product_info', 'parameter', 'value']
    list_filter = ['product_info', 'parameter']
