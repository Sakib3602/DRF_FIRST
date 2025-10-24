from django.urls import path
from .views import Products, SingleProduct , Categories

urlpatterns = [
    path('', Products.as_view(), name = 'all_products'),
    path('<int:pk>/', SingleProduct.as_view(), name = 'single_products'),
    path('cat/<int:id>', Categories.as_view(), name = 'single_category'),
    
]