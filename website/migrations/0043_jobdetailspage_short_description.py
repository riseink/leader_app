# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-26 18:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0042_careerspage'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobdetailspage',
            name='short_description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]