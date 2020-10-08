from django.contrib import admin

from shop.models import Shop, Category, Product, Parameter, ProductParameter


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class ShopAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ShopAdmin(admin.ModelAdmin):
    pass


@admin.register(Parameter)
class ShopAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductParameter)
class ShopAdmin(admin.ModelAdmin):
    pass
