# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-11 10:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20171111_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='data',
            field=models.CharField(default='', max_length=500),
        ),
    ]
