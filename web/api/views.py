from django.shortcuts import render
from api.serializers import ProductSerializer, SliderSerializer, CategorySerializer, OrderSerializer, UserSerializer
from api.models.product import Product
from api.models.banners import Slider
from api.models.category import Category
from api.models.filters import ProductFilter
from rest_framework import viewsets
from rest_framework import filters
from api.models.pagination import ProductListPagination
from api.models.order import Order
from api.models.user import User


# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().filter(enabled=True)
    serializer_class = ProductSerializer
    pagination_class = ProductListPagination
    http_method_names = ['get']
    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter)
    filter_class = ProductFilter
    ordering_fields = ('time_add', 'price', 'is_preorder', 'title')
    lookup_field = 'url'


class SliderViewSet(viewsets.ModelViewSet):
    queryset = Slider.objects.all().filter(enabled=True)
    serializer_class = SliderSerializer
    http_method_names = ['get']


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().filter(enabled=True)
    serializer_class = CategorySerializer
    http_method_names = ['get']
    lookup_field = 'url'


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
