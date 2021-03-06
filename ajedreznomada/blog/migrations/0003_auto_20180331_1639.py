# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-31 16:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180331_0801'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categorias'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['created_at'], 'verbose_name_plural': 'Publicaciones'},
        ),
        migrations.AddField(
            model_name='post',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='¿Esta activo?'),
        ),
    ]
