# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-24 11:31
from __future__ import unicode_literals

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('user_registration', '0002_auto_20170724_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]