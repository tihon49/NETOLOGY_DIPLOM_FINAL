from django.urls import path, include

from shop.views import ShopsListView, ShopDetailView, ShopCreateView, ShopUpdateView

urlpatterns = [
    path('shop/', ShopDetailView.as_view(), name='shop_detail'),
    path('shop/update/<int:pk>', ShopUpdateView.as_view(), name='shop_update'),
    path('shop/list/', ShopsListView.as_view(), name='shops_list_view'),
    path('shop/create', ShopCreateView.as_view(), name='shop_create'),
]

