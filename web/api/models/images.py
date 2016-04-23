from django.db import models

class ProductImage(models.Model):

    title = models.CharField(max_length=255, verbose_name='Название')
    image = models.ImageField(upload_to='img/%Y/%m/%d/')
    thumb = models.ImageField(upload_to='img/%Y/%m/%d/thumb/')

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        storage, path = self.image.storage, self.image.path
        thumb_storage, thumb_path = self.thumb.storage, self.thumb.path
        super(models.Model, self).delete(*args, **kwargs)
        thumb_storage.delete(thumb_path)
        storage.delete(path)

    def getUrl(self):
        return self.image

    class Meta:
        app_label = 'api'
        verbose_name = 'Изображение'
        verbose_name_plural = 'Иображения'

class SliderImage(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    image = models.ImageField(upload_to='img/%Y/%m/%d/')
    link = models.CharField(max_length=255, verbose_name='Ссылка')

    class Meta:
        app_label = 'api'
        verbose_name = 'Изображение для Слайдера'
        verbose_name_plural = 'Изображение для Слайдера'




