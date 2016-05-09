from django.db import models
from .images import Image
from .category import Category
from .seo_block import SeoBlock
from .sale import Sale


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, verbose_name='Название')
    url = models.CharField(max_length=255, verbose_name='Транслитерация', unique=True)
    category = models.ForeignKey(Category, related_name='category', on_delete=models.SET_NULL,
                                 null=True, verbose_name='Категория')
    description = models.TextField(verbose_name='СЕО описание', blank=True)

    title_image = models.ForeignKey(Image, on_delete=models.SET_NULL, blank=True,
                                     null=True, verbose_name='Главное изображение')

    gallery = models.ManyToManyField(Image, related_name='gallery', blank=True,
                                      verbose_name='Изображения')

    price = models.FloatField(verbose_name='Цена')
    enabled = models.BooleanField(verbose_name='Активный')
    seo_block = models.ForeignKey(SeoBlock, related_name='seo', on_delete=models.SET_NULL,
                                  null=True, verbose_name='Сео блок')
    time_add = models.DateTimeField(auto_now_add=True, editable=False, blank=True)

    sales = models.ManyToManyField(Sale, related_name='sale_pk', blank=True, verbose_name='Акции')

    is_new = models.BooleanField(verbose_name='Новинка')
    is_preorder = models.BooleanField(verbose_name='Предзаказ')
    is_sale = models.BooleanField(verbose_name='Отображать акции')

    def __str__(self):
        return self.title

    class Meta:
        app_label = 'api'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
