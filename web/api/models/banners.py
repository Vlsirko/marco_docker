from django.db import models
from .images import SliderImage


class Slider(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    #url = models.CharField(max_length=255)
    enabled = models.BooleanField(verbose_name='Активный')
    gallery = models.ManyToManyField(SliderImage, related_name='gallery', blank=True,
                                     verbose_name='Изображения 800x300')
    def __str__(self):
        return self.title

    class Meta:
        app_label = 'api'
        verbose_name = 'Cлайдер'
        verbose_name_plural = 'Слайдер'
