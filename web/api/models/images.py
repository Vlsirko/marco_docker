from django.db import models
from django.contrib.contenttypes.admin import GenericTabularInline
from django.contrib.contenttypes.fields import GenericForeignKey, ContentType
from marco.settings import IMAGE_SETTINGS
from django import forms
from django.utils.html import format_html


class Image(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    image = models.ImageField(upload_to='images/')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        """
        Удаляет изображение
        """
        storage, path = self.image.storage, self.image.path
        super(Image, self).delete(*args, **kwargs)
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


class ImageFieldDecorator:
    """
    Декоратор который форматирует url изображения что-бы оно корректно
    отображалось
    """
    def __init__(self, html=False, height='-', width='-'):
        """
        :param html: bool если установлен в True, вернет ссылку обернутую в тег <img>
        :param height: int высота изображения
        :param width: int ширина изображения
        """
        self.html, self.height, self.width = html, width, height

    def __call__(self, decorated_func):

        def decorated(field):

            image_path = decorated_func(field)

            if not image_path:
                image_path = IMAGE_SETTINGS['no_image']

            return format_html(self._make_pattern().format(**{
                'host': IMAGE_SETTINGS['server_host'],
                'height': self.height,
                'width': self.width,
                'path': image_path
            }))

        return decorated

    def _make_pattern(self):
        pattern = '{host}/{path}'
        if self.height != '-' or self.width != '-':
            pattern = '{host}/{width}/{height}/{path}'
        if self.html is True:
            pattern = '<img src="{0}" alt="thumb"/>'.format(pattern)
        return pattern
