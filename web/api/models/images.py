from django.db import models
from marco.settings import IMAGE_SETTINGS


class ProductImage(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    image = models.ImageField(upload_to='product/img/%Y/%m/%d/')

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        storage, path = self.image.storage, self.image.path
        super(models.Model, self).delete(*args, **kwargs)
        storage.delete(path)

    def path(self):
        thumb_sizes = IMAGE_SETTINGS['product']
        return '{0}/{1}/{2}/{3}'.format(IMAGE_SETTINGS['server_host'], thumb_sizes['height'], thumb_sizes['width'],
                                        self.image.name)

    def thumb(self):
        thumb_sizes = IMAGE_SETTINGS['product']['thumb']
        return '{0}/{1}/{2}/{3}'.format(IMAGE_SETTINGS['server_host'], thumb_sizes['height'], thumb_sizes['width'],
                                        self.image.name)

    class Meta:
        app_label = 'api'
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


class SliderImage(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    image = models.ImageField(upload_to='img/%Y/%m/%d/')
    link = models.CharField(max_length=255, verbose_name='Ссылка')

    def __str__(self):
        return self.title

    def path(self):
        thumb_sizes = IMAGE_SETTINGS['slider']
        return '{0}/{1}/{2}/{3}'.format(IMAGE_SETTINGS['server_host'], thumb_sizes['height'], thumb_sizes['width'],
                                        self.image.name)

    class Meta:
        app_label = 'api'
        verbose_name = 'Изображение для Слайдера'
        verbose_name_plural = 'Изображение для Слайдера'
