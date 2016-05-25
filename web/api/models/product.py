from django.db import models
from .images import Image
from .category import Category
from .seo_block import SeoBlock
from .sale import Sale
from marco.settings import IMAGE_SETTINGS
from django.contrib.contenttypes.models import ContentType


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, verbose_name='Название')
    url = models.CharField(max_length=255, verbose_name='Транслитерация', unique=True)
    category = models.ForeignKey(Category, related_name='category', on_delete=models.SET_NULL,
                                 null=True, verbose_name='Категория')
    description = models.TextField(verbose_name='Описание товара', blank=True)

    _title_image = models.ImageField(upload_to='product/img/%Y/%m/%d/', verbose_name='Главное изображение')

    price = models.FloatField(verbose_name='Цена')
    enabled = models.BooleanField(verbose_name='Активный')

    time_add = models.DateTimeField(auto_now_add=True, editable=False, blank=True)

    sales = models.ManyToManyField(Sale, related_name='sale_pk', blank=True, verbose_name='Акции')

    is_new = models.BooleanField(verbose_name='Новинка')
    is_preorder = models.BooleanField(verbose_name='Предзаказ')
    is_sale = models.BooleanField(verbose_name='Отображать акции')

    def __str__(self):
        return self.title

    @property
    def gallery(self):
        content_type = ContentType.objects.get(app_label='api', model='Product')
        return Image.objects.all().filter(object_id=self.id, content_type=content_type)

    @property
    def title_image(self):
        return '{0}/{1}'.format(IMAGE_SETTINGS['server_host'], self._title_image.name)

    class Meta:
        app_label = 'api'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
