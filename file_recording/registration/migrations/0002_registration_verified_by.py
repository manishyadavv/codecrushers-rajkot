# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-28 20:48
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='verified_by',
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.Admin'),
        ),
    ]
