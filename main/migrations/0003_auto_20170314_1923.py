# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-14 17:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_horseforsale_date_of_listing'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='horseforsale',
            options={'ordering': ['date_of_listing', 'name'], 'verbose_name': 'Кон за продажба', 'verbose_name_plural': 'Коне за продажба'},
        ),
        migrations.AddField(
            model_name='horseforsale',
            name='video_embed_code',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='horseforsale',
            name='name',
            field=models.CharField(max_length=128, verbose_name='Име'),
        ),
    ]
