# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-05 19:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='elfs',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, max_length=70, unique=True),
            preserve_default=False,
        ),
    ]