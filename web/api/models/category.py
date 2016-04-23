from  mptt.models import MPTTModel, TreeForeignKey
from django.db import models
from .seo_block import SeoBlock

class Category(MPTTModel):
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    parent = TreeForeignKey('self', blank=True, null=True, verbose_name="Родитель", related_name='child',  db_index=True)
    enabled = models.BooleanField()
    seo_block = models.ForeignKey(SeoBlock, on_delete=models.SET_NULL, null=True,
                                  verbose_name='Сео блок')

    def __str__(self):
        return self.title

    class Meta:
        app_label = 'api'
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'