from django.db import models
from django.contrib.contenttypes.admin import GenericTabularInline
from django.contrib.contenttypes.fields import GenericForeignKey, ContentType
from marco.settings import IMAGE_SETTINGS
from django import forms


class Image(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    image = models.ImageField(upload_to='product/img/%Y/%m/%d/')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        storage, path = self.image.storage, self.image.path
        models.Model(models.Model, self).delete(*args, **kwargs)
        storage.delete(path)

    def path(self):
        return '{0}/{1}'.format(IMAGE_SETTINGS['server_host'], self.image.name)

    class Meta:
        app_label = 'api'
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


class ImagePreviewWidget(forms.FileInput):
    """
    Виджет для превью изображения
    """

    type = 'file'

    def render(self, name, value, attrs=None):
        html = ''
        if value is not None:
            from marco.settings import IMAGE_SETTINGS
            html += """<a href='{0}/{1}'>
                        <img src="{0}/128/128/{1}">
                    </a>""".format(IMAGE_SETTINGS['server_host'], value)

        return html + super(ImagePreviewWidget, self).render(name, value, attrs)


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        widgets = {
            'image': ImagePreviewWidget()
        }
        fields = '__all__'


class ImageInline(GenericTabularInline):
    model = Image
    extra = 0
    form = ImageForm
