from rest_framework import filters
from .product import Product


class ProductFilter(filters.FilterSet):
    class Meta:
        model = Product
        fields = ['category__url']
