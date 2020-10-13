from django.urls import path
from rest_framework import routers

from buyer.views import OrderSerializerView, ItemsInOrderView
from shop.views import ShopDetailView, ShopCreateView, ShopsListView, CategoryListView, ProductListView

router = routers.DefaultRouter()

# /api/v1/buyer/
# /api/v1/buyer/update/<int:item_id>/
router.register('cart/update', ItemsInOrderView)

urlpatterns = [
    path('shop/', ShopDetailView.as_view(), name='shop_detail'),
    path('shop/list/', ShopsListView.as_view(), name='shops_list_view'),
    path('shop/create', ShopCreateView.as_view(), name='shop_create'),
    path('category/', CategoryListView.as_view(), name='category_list'),
    path('products/', ProductListView.as_view(), name='products'),
    path('cart/', OrderSerializerView.as_view(), name='order'),
]

urlpatterns += router.urls
