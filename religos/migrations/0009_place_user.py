# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-23 15:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('religos', '0008_auto_20170121_1352'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
