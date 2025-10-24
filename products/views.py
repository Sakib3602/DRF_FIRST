from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProductSerializer, CategorySerializer
from .models import Product, Category
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.
# @api_view(["GET","POST"])
# def Products(request):
#     if request.method == 'GET':
#         pro = Product.objects.all()
#         serializer = ProductSerializer(pro , many = True,context={'request': request})
#         return Response(serializer.data)
#     if request.method == 'POST':
#         serializer = ProductSerializer(data=request.data,context={'request': request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Products(APIView):
    def get(self, request):
        pro = Product.objects.all()
        serializer = ProductSerializer(pro , many = True,context={'request': request})
        return Response(serializer.data)

    def post(self,request):
        serializer = ProductSerializer(data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)







# @api_view(["GET","PUT","DELETE"])
# def SingleProduct(request, pk):
#     if request.method == 'GET':
#         try:
#             pro = Product.objects.get(pk=pk)
#         except Product.DoesNotExist:
#             return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
#         serializer = ProductSerializer(pro,context={'request': request})
#         return Response(serializer.data)
    
#     if request.method =="PUT":
#         serializer = ProductSerializer(data=request.data,context={'request': request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     if request.method == "DELETE":
#         try:
#             pro = Product.objects.get(pk=pk)
#         except Product.DoesNotExist:
#             return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
#         pro.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
  
class SingleProduct(APIView): 
    def get(self, request, pk):
        try:
            pro = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(pro, context ={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        try:
            pro = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ProductSerializer(pro, data = request.data, context = {'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
# @api_view(["GET"])
# def Categories(request,id):
#     try:
#         cat = Category.objects.get(id=id)
#     except Category.DoesNotExist:
#         return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == "GET":
#         serializer = CategorySerializer(cat,context={'request': request})
#         return Response(serializer.data)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class Categories(APIView):
    def get(self, request, id):
        try:
            cat = Category.objects.get(id=id)
        except Category.DoesNotExist:
            return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CategorySerializer(cat, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)