# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-14 05:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('religos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='add_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
