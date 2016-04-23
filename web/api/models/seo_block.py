from django.db import models

class SeoBlock(models.Model):
    title = models.CharField(max_length=255, verbose_name='Сео Название')
    meta = models.CharField(max_length=255, verbose_name='СЕО мета тег')
    description = models.TextField(verbose_name='СЕО описание')

    def __str__(self):
        return self.title

    class Meta:
        app_label = 'api'
        verbose_name_plural = 'SEO блоки'
        verbose_name = 'SEO блок'