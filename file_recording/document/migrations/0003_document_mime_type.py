# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-29 06:24
from __future__ import unicode_literals

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0002_auto_20170729_0620'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='mime_type',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
