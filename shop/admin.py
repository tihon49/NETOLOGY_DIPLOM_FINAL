from django.contrib import admin

from shop.models import (Shop, Category,Product, ProductInfo,
                         Parameter, ProductParameter)


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'state' ]
    list_display_links = ['name', 'user', 'state' ]
    list_filter = ['state']

@admin.register(Category)
class ShopAdmin(admin.ModelAdmin):
    pass

@admin.register(Product)
class ShopAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']

@admin.register(ProductInfo)
class ShopAdmin(admin.ModelAdmin):
    list_display = ['product', 'model', 'shop', 'quantity', 'price', 'price_rrc']

@admin.register(Parameter)
class ShopAdmin(admin.ModelAdmin):
    pass

@admin.register(ProductParameter)
class ShopAdmin(admin.ModelAdmin):
    list_display = ['product_info', 'parameter', 'value']