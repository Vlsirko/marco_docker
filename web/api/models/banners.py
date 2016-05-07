from django.db import models
from .images import Image


class Slider(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    enabled = models.BooleanField(verbose_name='Активный')
    gallery = models.ManyToManyField(Image, related_name='gallery_pk', blank=True,
                                     verbose_name='Изображения 800x400')

    def __str__(self):
        return self.title

    def slides(self):
        slides = self.gallery.all()
        result_set = []

        if slides:
            from marco.settings import IMAGE_SETTINGS
            for image in slides:
                result_set.append(image.get_path(**IMAGE_SETTINGS['slider']))

        return result_set

    class Meta:
        app_label = 'api'
        verbose_name = 'Cлайдер'
        verbose_name_plural = 'Слайдер'
