# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-24 11:29
from __future__ import unicode_literals

import datetime

from django.db import migrations
from django.db import models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('user_registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='birth_date',
            field=models.DateField(default=datetime.datetime(
                2017, 7, 24, 11, 29, 4, 714068, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
