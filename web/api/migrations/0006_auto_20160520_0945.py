# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-20 09:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20160520_0903'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='product_set',
        ),
        migrations.RemoveField(
            model_name='order',
            name='status',
        ),
    ]