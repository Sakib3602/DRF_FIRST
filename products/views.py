from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProductSerializer, CategorySerializer
from .models import Product, Category
from rest_framework import status

# Create your views here.
@api_view(["GET","POST"])
def Products(request):
    if request.method == 'GET':
        pro = Product.objects.all()
        serializer = ProductSerializer(pro , many = True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(["GET"])
def SingleProduct(request, pk):
    try:
        pro = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ProductSerializer(pro)
        return Response(serializer.data, status=status.HTTP_200_OK)