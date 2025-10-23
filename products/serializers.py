from rest_framework import serializers
from .models import Product, Category
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
    
   
class ProductSerializer(serializers.ModelSerializer):
    # category = CategorySerializer()  # nested representation (full category te ja ase sob dekhaibo)
    # category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())  # sudhu primary key dekhaibo
    # category = serializers.StringRelatedField() # sudhu category name dekhaibo
    # category_id = serializers.PrimaryKeyRelatedField(
    #     queryset=Category.objects.all(), write_only=True
    # )
  

    # Optional: keep read-only nested data for GET
    # category  = CategorySerializer()
    class Meta:
        model = Product
        fields = "__all__"
    category = serializers.HyperlinkedRelatedField(
        queryset=Category.objects.all(),
        view_name='single_category',
        lookup_field='id'
    )
    