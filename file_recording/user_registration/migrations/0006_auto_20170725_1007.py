# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-25 10:07
from __future__ import unicode_literals

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('user_registration', '0005_auto_20170725_1006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='uid',
            field=models.CharField(blank=True, max_length=40, unique=True),
        ),
    ]
