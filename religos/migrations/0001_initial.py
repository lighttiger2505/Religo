# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-14 02:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=200)),
            ],
        ),
    ]
