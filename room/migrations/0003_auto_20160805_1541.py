# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-05 14:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0002_auto_20160803_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='name',
            field=models.CharField(max_length=128, unique=True),
        ),
    ]
