from django.contrib import admin
from api.models.product import Product, ProductForm
from api.models.category import Category
from api.models.images import ImageInline
from api.models.banners import Slider
from api.models.seo_block import SeoBlockInline
from api.models.sale import Sale, SaleForm
from api.models.order import Order, OrderInline
from api.models.user import User

from django_mptt_admin.admin import DjangoMpttAdmin


class CategoryAdmin(DjangoMpttAdmin):
    tree_title_field = 'title'
    # tree_display = ('name', 'slug', 'created|date')  # name тут указывать необязательно

    inlines = [
        SeoBlockInline
    ]

    class Meta:
        model = Category


class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
        SeoBlockInline
    ]
    form = ProductForm
    filter_horizontal = ['sales']
    list_filter = ('is_new', 'is_sale', 'is_preorder', 'enabled')
    search_fields = ('title', 'id')
    list_display = ('title_image_thumb', 'title', 'category', 'price', 'time_add', 'enabled')
    list_display_links = ('title', 'title_image_thumb')

class SliderAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline
    ]


class SaleAdmin(admin.ModelAdmin):
    form = SaleForm


# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Slider, SliderAdmin)
admin.site.register(Sale, SaleAdmin)
admin.site.register(Order, OrderInline)
admin.site.register(User)
