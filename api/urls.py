from django.urls import path

from shop.views import ShopDetailView, ShopCreateView, ShopsListView, CategoryListView, ProductListView # ProductView,

urlpatterns = [
    path('shop/', ShopDetailView.as_view(), name='shop_detail'),
    path('shop/list/', ShopsListView.as_view(), name='shops_list_view'),
    path('shop/create', ShopCreateView.as_view(), name='shop_create'),
    path('category/', CategoryListView.as_view(), name='category_list'),
    path('products/', ProductListView.as_view(), name='products'),
]
