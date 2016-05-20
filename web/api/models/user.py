from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name='Имя')
    email = models.EmailField(verbose_name='Email')

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'api'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'