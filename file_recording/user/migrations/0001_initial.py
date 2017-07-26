# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 16:02
from __future__ import unicode_literals

import django.core.validators
import django.db.models.deletion
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('auto_logout', models.NullBooleanField(default=None)),
                ('logout_at', models.DateTimeField(default=None, null=True)),
                ('session_id', models.CharField(max_length=128)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[
                 (1, 'Male'), (2, 'Female'), (3, 'Others')], max_length=10)),
                ('father_name', models.CharField(max_length=100)),
                ('spouse_name', models.CharField(
                    blank=True, max_length=100, null=True)),
                ('pan_number', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(
                    message='Pan number not valid.', regex='^[A-Z]{5}[0-9]{4}[A-Z]{1}$')])),
                ('aadhar_no', models.CharField(max_length=12, validators=[
                 django.core.validators.RegexValidator(message='Aadhar number not valid.', regex='^[0-9]{12}$')])),
                ('birth_date', models.DateField()),
                ('phone', models.CharField(max_length=13, unique=True, validators=[django.core.validators.RegexValidator(
                    message='Phone number not valid.', regex='^(?:\\+?91)?[789]\\d{9,10}$')])),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('address', models.TextField()),
                ('password', models.CharField(max_length=128)),
                ('uid', models.CharField(blank=True, max_length=40, unique=True)),
                ('is_login', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='session',
            name='user',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to='user.User'),
        ),
    ]
