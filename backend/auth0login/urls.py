from django.urls import path, include
from . import views

urlpatterns = [
    path('auth', views.index),
    path('dashboard', views.dashboard),
    path('logout', views.logout),
    path('', include('django.contrib.auth.urls')),
    path('', include('social_django.urls')),
]
