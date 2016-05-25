from django.contrib import admin
from api.models.product import Product
from api.models.category import Category
from api.models.images import ImageInline
from api.models.banners import Slider
from api.models.seo_block import SeoBlock
from api.models.sale import Sale
from api.models.order import Order, OrderInline
from api.models.user import User

from django_mptt_admin.admin import DjangoMpttAdmin


class CategoryAdmin(DjangoMpttAdmin):
    tree_title_field = 'title'
    #tree_display = ('name', 'slug', 'created|date')  # name тут указывать необязательно

    class Meta:
        model = Category

class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline
    ]

class SliderAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline
    ]

# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Slider, SliderAdmin)
admin.site.register(Sale)
admin.site.register(SeoBlock)
admin.site.register(Order, OrderInline)
admin.site.register(User)

