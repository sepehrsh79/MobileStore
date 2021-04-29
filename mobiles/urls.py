from django.urls import path, include
from .views import create_mobile

urlpatterns = [
    path('', create_mobile)
]