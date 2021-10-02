from typing import Text
from django.urls import path
from .views import *

urlpatterns = [
    path('',home, name='dashboard'),
    path('test',test),
    path('help',help)
    ]