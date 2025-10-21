from django.urls import path, include
from .views import Products
urlpatterns = [
    path('', Products, name = 'all_products'),
]