# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-22 18:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0030_newslandingpage_newspage'),
    ]

    operations = [
        migrations.AddField(
            model_name='newspage',
            name='author',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]