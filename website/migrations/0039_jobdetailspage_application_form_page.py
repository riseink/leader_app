# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-24 20:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('website', '0038_auto_20181024_2001'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobdetailspage',
            name='application_form_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page'),
        ),
    ]