# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-27 08:49
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('schemes', '0004_auto_20170726_1602'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('is_verified', models.BooleanField(default=False)),
                ('is_valid', models.NullBooleanField(default=None)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('flat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                           related_name='registerations', to='schemes.Flat')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                           related_name='applications', to='user.User')),
            ],
        ),
    ]