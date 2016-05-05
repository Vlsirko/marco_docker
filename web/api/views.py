from django.shortcuts import render
from api.serializers import ProductSerializer, SliderSerializer, CategorySerializer
from api.models.product import Product
from api.models.banners import Slider
from api.models.category import Category
from api.models.filters import ProductFilter
from rest_framework import viewsets
from rest_framework import filters
from api.models.pagination import ProductListPagination

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().filter(enabled=True)
    serializer_class = ProductSerializer
    pagination_class = ProductListPagination
    http_method_names = ['get']
    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter)
    filter_class = ProductFilter
    ordering_fields = ('time_add',)


class SliderViewSet(viewsets.ModelViewSet):
    queryset = Slider.objects.all().filter(enabled=True)
    serializer_class = SliderSerializer
    http_method_names = ['get']


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().filter(enabled=True)
    serializer_class = CategorySerializer
    http_method_names = ['get']
