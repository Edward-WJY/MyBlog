# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-01-16 04:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_content_html'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_md',
            field=models.BooleanField(default=False, verbose_name='markdown语法'),
        ),
    ]