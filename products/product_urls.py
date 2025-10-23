from django.urls import path
from .views import Products, SingleProduct , Categories

urlpatterns = [
    path('', Products, name = 'all_products'),
    path('<int:pk>/', SingleProduct, name = 'single_products'),
    path('cat/<int:id>', Categories, name = 'single_category'),
    
]