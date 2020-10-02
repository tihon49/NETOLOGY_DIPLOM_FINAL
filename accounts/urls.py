from django.urls import path, include
from . import views


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('profile/', views.profileView, name='profile_view')
]
