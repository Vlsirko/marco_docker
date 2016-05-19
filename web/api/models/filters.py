import rest_framework_filters as filters
import django_filters
from .product import Product


class IntegerListFilter(django_filters.Filter):
    def filter(self,qs,value):
        if value not in (None,''):
            integers = [int(v) for v in value.split(',')]
            return qs.filter(**{'%s__%s'%(self.name, self.lookup_type):integers})
        return qs

class ProductFilter(filters.FilterSet):
    ids = IntegerListFilter(name="id", lookup_type='in')
    class Meta:
        model = Product
        fields = ['category__url', 'is_new', 'is_sale', 'ids']
