# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-23 18:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_author_nationality'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='nationality',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]