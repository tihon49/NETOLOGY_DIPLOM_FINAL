from django.contrib import admin

from api.models import (Shop, Category, Product, ProductParameter,
                        ProductInfo, Parameter, Contact, Order,
                        OrderItem, ConfirmEmailToken)


@admin.register(Shop)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductInfo)
class UserAdmin(admin.ModelAdmin):
    list_display = ['product', 'model']
    list_display_links = ['model', 'product']
    list_filter = ['product']


@admin.register(Parameter)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductParameter)
class UserAdmin(admin.ModelAdmin):
    list_display = ['product_info', 'parameter', 'value']


@admin.register(Contact)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(OrderItem)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(ConfirmEmailToken)
class UserAdmin(admin.ModelAdmin):
    pass
