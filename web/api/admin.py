from django.contrib import admin
from api.models import Product, Category, Image, SeoBlock
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
admin.site.register(SeoBlock)

