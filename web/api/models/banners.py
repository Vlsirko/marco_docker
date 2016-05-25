from django.db import models
from django.contrib.contenttypes.models import ContentType
from .images import Image


class Slider(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    enabled = models.BooleanField(verbose_name='Активный')

    def __str__(self):
        return self.title

    @property
    def gallery(self):
        content_type = ContentType.objects.get(app_label='api', model='Slider')
        return Image.objects.all().filter(object_id=self.id, content_type=content_type)

    class Meta:
        app_label = 'api'
        verbose_name = 'Cлайдер'
        verbose_name_plural = 'Слайдер'
