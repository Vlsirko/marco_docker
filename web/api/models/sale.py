from django.db import models
from .images import Image


class Sale(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name='Описание')
    _image = models.ForeignKey(Image, on_delete=models.SET_NULL, blank=True,
                              null=True, verbose_name='Изображение')
    time_start = models.DateTimeField(verbose_name='Дата старта', blank=True)
    time_end = models.DateTimeField(verbose_name='Дата конца', blank=True)

    def image(self):
        if self._image:
            from marco.settings import IMAGE_SETTINGS
            return {
                'thumb': self._image.get_path(**IMAGE_SETTINGS['sale']['thumb']),
                'path' : self._image.get_path()
            }

    def __str__(self):
        return self.title

    class Meta:
        app_label = 'api'
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'
