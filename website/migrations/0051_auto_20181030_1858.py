# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-30 18:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0050_auto_20181029_2017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutpage',
            name='violator',
        ),
        migrations.RemoveField(
            model_name='careerspage',
            name='violator',
        ),
        migrations.RemoveField(
            model_name='contactpage',
            name='violator',
        ),
        migrations.RemoveField(
            model_name='disciplinepage',
            name='violator',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='violator',
        ),
        migrations.RemoveField(
            model_name='jobdetailspage',
            name='violator',
        ),
        migrations.RemoveField(
            model_name='leadershippage',
            name='violator',
        ),
        migrations.RemoveField(
            model_name='newslandingpage',
            name='violator',
        ),
        migrations.RemoveField(
            model_name='newspage',
            name='violator',
        ),
        migrations.RemoveField(
            model_name='tinderpage',
            name='violator',
        ),
        migrations.RemoveField(
            model_name='workpage',
            name='violator',
        ),
        migrations.RemoveField(
            model_name='worksamplepage',
            name='violator',
        ),
    ]