# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 03:39
from __future__ import unicode_literals

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('user_registration', '0010_auto_20170726_0331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]