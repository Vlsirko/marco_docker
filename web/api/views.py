from django.shortcuts import render
from api.serializers import ProductSerializer, SliderSerializer, CategorySerializer
from api.models.product import Product
from api.models.banners import Slider
from api.models.category import Category
from rest_framework import viewsets


# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ['get']

    def get_queryset(self, request):
        if 'category' in request.query_params:
            return Product.objects.all().filter(category__url=request.query_params['category'], enabled=True)
        return Product.objects.all().filter(enabled=True)


class SliderViewSet(viewsets.ModelViewSet):
    queryset = Slider.objects.all().filter(enabled=True)
    serializer_class = SliderSerializer
    http_method_names = ['get']


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().filter(enabled=True)
    serializer_class = CategorySerializer
    http_method_names = ['get']

