from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view()
def Products(request):
    return Response({"message": "List of products"})