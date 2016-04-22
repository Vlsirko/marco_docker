from django.shortcuts import render
from api.serializers import ProductSerializer
from api.models import Product
from rest_framework import viewsets


# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ['get']