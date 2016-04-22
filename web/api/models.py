from django.db import models
import mptt

# Create your models here.

class SeoBlock(models.Model):
    title = models.CharField(max_length=255, verbose_name='Сео Название')
    meta = models.CharField(max_length=255, verbose_name='СЕО мета тег')
    description = models.TextField(verbose_name='СЕО описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'SEO блоки'
        verbose_name = 'SEO блок'


class Image(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    image = models.ImageField(upload_to='img/%Y/%m/%d/')
    thumb = models.ImageField(upload_to='img/%Y/%m/%d/thumb/')

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        storage, path = self.image.storage, self.image.path
        thumb_storage, thumb_path = self.thumb.storage, self.thumb.path
        super(Image, self).delete(*args, **kwargs)
        thumb_storage.delete(thumb_path)
        storage.delete(path)

    def getUrl(self):
        return self.image

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Иображения'


class Category(models.Model):
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    parent = models.ForeignKey('self', blank=True, null=True, verbose_name="Родитель", related_name='child')
    enabled = models.BooleanField()
    seo_block = models.ForeignKey(SeoBlock, on_delete=models.SET_NULL, null=True,
                                  verbose_name='Сео блок')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'


mptt.register(Category)


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, verbose_name='Название')
    url = models.CharField(max_length=255, verbose_name='Транслитерация')
    category = models.ForeignKey(Category, related_name='category', on_delete=models.SET_NULL,
                                 null=True, verbose_name='Категория')
    title_image = models.ForeignKey(Image, on_delete=models.SET_NULL, blank=True,
                                    null=True, verbose_name='Главное изображение')
    gallery = models.ManyToManyField(Image, related_name='gallery', blank=True,
                                     verbose_name='Изображения')
    price = models.FloatField(verbose_name='Цена')
    enabled = models.BooleanField(verbose_name='Активный')
    seo_block = models.ForeignKey(SeoBlock, related_name='seo', on_delete=models.SET_NULL,
                                  null=True, verbose_name='Сео блок')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
