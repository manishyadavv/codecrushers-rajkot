# -*- coding: utf-8 -*-
import hashlib
from datetime import datetime

from django.db import models


class User(models.Model):
    GENDERS = (
        (1, 'Male'),
        (2, 'Female'),
        (3, 'Others')
    )
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDERS)
    father_name = models.CharField(max_length=100)
    spouse_name = models.CharField(max_length=100, blank=True, null=True)
    pan_number = models.CharField(max_length=10)
    aadhar_no = models.CharField(max_length=12)
    birth_date = models.DateField()
    phone = models.CharField(max_length=10, unique=True,
                             validators=[RegexValidator(regex=r'^(?:\+?91)?[789]\d{9,10}$',
                                                        message='phone number not valid',), )
    email = models.CharField(max_length=50, unique=True)
    address = models.TextField()
    password = models.CharField(max_length=128)
    uid = models.CharField(max_length=40, unique=True, blank=True)
    is_login = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.uid == '':
            self.uid = hashlib.sha1(
                (str(self.email) + str(self.phone)).encode('utf-8')).hexdigest()
        super(User, self).save(*args, **kwargs)


class Session(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=False, blank=False)
    auto_logout = models.NullBooleanField(default=None)
    logout_at = models.DateTimeField(default=None, null=True)
    session_id = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.session_id == '':
            self.session_id = hashlib.sha512(
                str(datetime.now()).encode('utf-8')).hexdigest()
        super(Session, self).save(*args, **kwargs)
