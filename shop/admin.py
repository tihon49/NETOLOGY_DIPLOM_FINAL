from django.contrib import admin

from shop.models import Shop, Category, Product


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'url', 'user']
    list_display_links = ['id', 'name', 'url', 'user']


@admin.register(Category)
class ShopAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ShopAdmin(admin.ModelAdmin):
    pass


# @admin.register(Parameter)
# class ShopAdmin(admin.ModelAdmin):
#     pass
#
#
# @admin.register(ProductParameter)
# class ShopAdmin(admin.ModelAdmin):
#     pass
