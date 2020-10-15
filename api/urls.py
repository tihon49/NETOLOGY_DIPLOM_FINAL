from django.urls import path
from rest_framework import routers

from buyer.views import OrderSerializerView, ItemsInOrderView, AddItemInOrderView
from shop.views import (ShopBaseView, ShopCreateView, ShopsListView,
                        CategoryListView, ProductListView, ShopDetailView, ShopDetailView)

router = routers.DefaultRouter()

# /api/v1/cart/
# /api/v1/cart/update/<int:item_id>/
router.register('cart/update', ItemsInOrderView)
router.register('shop/detail', ShopDetailView, 'shop_detail')

urlpatterns = [
    path('shop/', ShopBaseView.as_view(), name='shop_detail'),
    path('shop/list/', ShopsListView.as_view(), name='shops_list_view'),
    path('shop/create/', ShopCreateView.as_view(), name='shop_create'),
    path('category/', CategoryListView.as_view(), name='category_list'),
    path('products/', ProductListView.as_view(), name='products'),
    path('cart/', OrderSerializerView.as_view(), name='order'),
    path('cart/add/', AddItemInOrderView.as_view(), name='add_item_in_order')
]

urlpatterns += router.urls
