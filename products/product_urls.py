from django.urls import path
from .views import Products, SingleProduct

urlpatterns = [
    path('', Products, name = 'all_products'),
    path('<int:pk>/', SingleProduct, name = 'single_products'),
]