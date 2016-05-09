from django.db import models
from marco.settings import IMAGE_SETTINGS


class Image(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    image = models.ImageField(upload_to='product/img/%Y/%m/%d/')

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        storage, path = self.image.storage, self.image.path
        models.Model(models.Model, self).delete(*args, **kwargs)
        storage.delete(path)

    def get_path(self, height='-', width='-'):
        return '{0}/{1}/{2}/{3}'.format(IMAGE_SETTINGS['server_host'], height, width,
                                        self.image.name)

    class Meta:
        app_label = 'api'
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
