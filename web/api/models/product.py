from django.db import models
from .images import ProductImage
from .category import Category
from .seo_block import SeoBlock

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, verbose_name='Название')
    url = models.CharField(max_length=255, verbose_name='Транслитерация')
    category = models.ForeignKey(Category, related_name='category', on_delete=models.SET_NULL,
                                 null=True, verbose_name='Категория')
    title_image = models.ForeignKey(ProductImage, on_delete=models.SET_NULL, blank=True,
                                    null=True, verbose_name='Главное изображение')
    gallery = models.ManyToManyField(ProductImage, related_name='gallery', blank=True,
                                     verbose_name='Изображения')
    price = models.FloatField(verbose_name='Цена')
    enabled = models.BooleanField(verbose_name='Активный')
    seo_block = models.ForeignKey(SeoBlock, related_name='seo', on_delete=models.SET_NULL,
                                  null=True, verbose_name='Сео блок')

    def __str__(self):
        return self.title

    class Meta:
        app_label = 'api'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'