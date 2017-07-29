# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-29 19:06
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20170729_1657'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='caste',
            field=models.IntegerField(
                choices=[(1, 'GENERAL'), (2, 'OBC'), (3, 'SC'), (4, 'ST')], default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='spouse_aadhar',
            field=models.CharField(blank=True, default='', max_length=12, validators=[
                                   django.core.validators.RegexValidator(message="Spouse's Aadhar number not valid.", regex='^[0-9]{12}$')]),
        ),
        migrations.AlterField(
            model_name='user',
            name='spouse_name',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
