# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-23 18:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20170522_2244'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='nationality',
            field=models.CharField(blank=True, default='Canada', max_length=50, null=True),
        ),
    ]
