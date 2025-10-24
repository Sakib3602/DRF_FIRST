from rest_framework import serializers
from .models import Product, Category
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
    
   
class ProductSerializer(serializers.ModelSerializer):   
    class Meta:
        model = Product
        fields = "__all__"
    category = serializers.HyperlinkedRelatedField(
        queryset=Category.objects.all(),
        view_name='single_category',
        lookup_field='id'
    )
    