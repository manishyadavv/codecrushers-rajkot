# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-29 14:53
from __future__ import unicode_literals

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.IntegerField(
                choices=[(1, 'Male'), (2, 'Female'), (3, 'Others')], max_length=10),
        ),
    ]
