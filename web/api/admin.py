from django.contrib import admin
from api.models.product import Product
from api.models.category import Category
from api.models.images import Image
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

# Register your models here.
admin.site.register(Product)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Image)
admin.site.register(Slider)
admin.site.register(Sale)
admin.site.register(SeoBlock)
admin.site.register(Order, OrderInline)
admin.site.register(User)

