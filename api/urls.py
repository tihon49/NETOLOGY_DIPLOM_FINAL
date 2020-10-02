from django.urls import path, include
from django_rest_passwordreset.views import reset_password_request_token, reset_password_confirm

from .views import (PartnerUpdate, RegisterAccount, LoginAccount,
                    CategoryView, ShopsListView, ProductInfoView, BasketView,
                    AccountDetails, ContactView, OrderView, PartnerState,
                    PartnerOrders, ConfirmAccount, UsersListView, UserDetailView, ShopDetailView)

urlpatterns = [
    path('base_auth/', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    path('token_auth/', include('djoser.urls.authtoken')),

    #FROM NETOLOGY EXAMPLE
    path('partner/update/', PartnerUpdate.as_view(), name='partner-update'),
    path('partner/state/', PartnerState.as_view(), name='partner-state'),
    path('partner/orders/', PartnerOrders.as_view(), name='partner-orders'),
    path('user/register/', RegisterAccount.as_view(), name='user-register'),
    path('user/register/confirm/', ConfirmAccount.as_view(), name='user-register-confirm'),
    path('user/list/', UsersListView.as_view(), name='users-list'),
    path('user/detail/<int:pk>', UserDetailView.as_view(), name='user-detail'),
    # path('user/details', AccountDetails.as_view(), name='user-details'),
    path('user/contact/', ContactView.as_view(), name='user-contact'),
    path('user/login/', LoginAccount.as_view(), name='user-login'),
    path('user/password_reset/', reset_password_request_token, name='password-reset'),
    path('user/password_reset/confirm/', reset_password_confirm, name='password-reset-confirm'),
    path('categories/', CategoryView.as_view(), name='categories'),
    path('shops/', ShopsListView.as_view(), name='shops'),
    path('shops/detail/<int:pk>', ShopDetailView.as_view(), name='shop_detail'),
    path('products/', ProductInfoView.as_view(), name='shops'),
    path('basket/', BasketView.as_view(), name='basket'),
    path('order/', OrderView.as_view(), name='order'),

]

