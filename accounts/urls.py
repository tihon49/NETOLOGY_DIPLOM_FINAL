from django.urls import path, include

from accounts.views import RestrictedApiView
from orders.views import registerView


urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')), #/auth/token/login/ to get token
    path('', include('rest_framework.urls')),
    path('reg/', registerView, name='register'),
    path('restricted/', RestrictedApiView.as_view()),

]
