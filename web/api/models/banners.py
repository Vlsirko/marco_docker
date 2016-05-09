from django.db import models
from .images import Image


class Slider(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    enabled = models.BooleanField(verbose_name='Активный')
    gallery = models.ManyToManyField(Image, related_name='gallery_pk', blank=True,
                                     verbose_name='Изображения 800x400')

    def __str__(self):
        return self.title

    class Meta:
        app_label = 'api'
        verbose_name = 'Cлайдер'
        verbose_name_plural = 'Слайдер'
