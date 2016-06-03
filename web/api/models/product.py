from django import forms
from django.contrib.contenttypes.models import ContentType
from django.db import models
from mptt.models import TreeForeignKey
from tinymce import models as tiny_mce_model
from .category import Category
from .images import Image, ImagePreviewWidget, ImageFieldDecorator
from .sale import Sale
from .seo_block import SeoBlock


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, verbose_name='Название', db_index=True)
    url = models.CharField(max_length=255, verbose_name='Транслитерация', unique=True)
    category = TreeForeignKey(Category, related_name='category', on_delete=models.SET_NULL,
                              null=True, verbose_name='Категория')
    description = tiny_mce_model.HTMLField(verbose_name='Описание товара', blank=True)

    _title_image = models.ImageField(upload_to='product/img/%Y/%m/%d/', verbose_name='Главное изображение')

    price = models.FloatField(verbose_name='Цена')
    enabled = models.BooleanField(verbose_name='Активный')

    time_add = models.DateTimeField(auto_now_add=True, editable=False, blank=True)

    sales = models.ManyToManyField(Sale, related_name='sale_pk', blank=True, verbose_name='Акции')

    is_new = models.BooleanField(verbose_name='Новинка')
    is_preorder = models.BooleanField(verbose_name='Предзаказ')
    is_sale = models.BooleanField(verbose_name='Отображать акции')
    pieces_left = models.IntegerField(verbose_name='Штук осталось', null=True, blank=True)

    def __str__(self):
        return self.title

    @property
    def gallery(self):
        content_type = ContentType.objects.get(app_label='api', model='Product')
        return Image.objects.all().filter(object_id=self.id, content_type=content_type)

    @property
    @ImageFieldDecorator()
    def title_image(self):
        return self._title_image.name

    @property
    @ImageFieldDecorator(html=True, height=64, width=64)
    def title_image_thumb(self):
        return self._title_image.name

    @property
    def seo_block(self):
        content_type = ContentType.objects.get(app_label='api', model='Product')
        return SeoBlock.objects.get(object_id=self.id, content_type=content_type)

    class Meta:
        app_label = 'api'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            '_title_image': ImagePreviewWidget()
        }
