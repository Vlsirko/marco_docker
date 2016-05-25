from mptt.models import MPTTModel, TreeForeignKey
from django.db import models
from django.contrib.contenttypes.models import ContentType
from .seo_block import SeoBlock


class Category(MPTTModel):
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255, unique=True)
    parent = TreeForeignKey('self', blank=True, null=True, verbose_name="Родитель", related_name='child', db_index=True)
    enabled = models.BooleanField()

    @property
    def seo_block(self):
        content_type = ContentType.objects.get(app_label='api', model='Category')
        return SeoBlock.objects.get(object_id=self.id, content_type=content_type)

    def __str__(self):
        return self.title

    class Meta:
        app_label = 'api'
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'
