from django.shortcuts import render
from api.serializers import ProductSerializer, SliderSerializer, CategorySerializer
from api.models.product import Product
from api.models.banners import Slider
from api.models.category import Category
from api.models.filters import ProductFilter
from rest_framework import viewsets
from rest_framework import filters


# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().filter(enabled=True)
    serializer_class = ProductSerializer
    http_method_names = ['get']
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = ProductFilter


class SliderViewSet(viewsets.ModelViewSet):
    queryset = Slider.objects.all().filter(enabled=True)
    serializer_class = SliderSerializer
    http_method_names = ['get']


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().filter(enabled=True)
    serializer_class = CategorySerializer
    http_method_names = ['get']
