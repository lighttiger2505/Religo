# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-17 15:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('religos', '0005_auto_20170117_0956'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='ocr_text',
            field=models.TextField(default='dummy', max_length=2000),
            preserve_default=False,
        ),
    ]
