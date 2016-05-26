from django.db import models
from django import forms
from .images import ImagePreviewWidget


class Sale(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='sale/img/%Y/%m/%d/', verbose_name='Изображение')
    time_start = models.DateTimeField(verbose_name='Дата старта', blank=True)
    time_end = models.DateTimeField(verbose_name='Дата конца', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        app_label = 'api'
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'


class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = '__all__'
        widgets = {
            'image': ImagePreviewWidget()
        }
