from django.db import models
from django.contrib.contenttypes.admin import GenericStackedInline
from django.contrib.contenttypes.fields import GenericForeignKey, ContentType
from tinymce import models as tiny_mce_model


class SeoBlock(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок СЕО', null=False, blank=False)
    meta_description = models.CharField(max_length=255, verbose_name='Мета описание СЕО', null=False, blank=False)
    keywords = models.TextField(max_length=255, verbose_name='Ключевые слова страницы', null=False, blank=False)
    description = tiny_mce_model.HTMLField(verbose_name='Описание', null=False, blank=False)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.title

    class Meta:
        app_label = 'api'
        verbose_name_plural = 'SEO блоки'
        verbose_name = 'SEO блок'


class SeoBlockInline(GenericStackedInline):
    model = SeoBlock
    max_num = 1