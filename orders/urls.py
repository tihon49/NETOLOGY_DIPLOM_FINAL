from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
    path('accounts/', include('accounts.urls')),
    path('register/', views.registerView, name='register_view'),

]
