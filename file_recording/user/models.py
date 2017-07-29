# -*- coding: utf-8 -*-
import hashlib
from datetime import datetime

from django.core.validators import RegexValidator
from django.db import models

from file_recording.employee.models import Admin


class User(models.Model):
    GENDERS = (
        (1, 'Male'),
        (2, 'Female'),
        (3, 'Others')
    )
    CASTE = (
            (1, 'GENERAL'),
            (2, 'OBC'),
            (3, 'SC'),
            (4, 'ST')
    )
    name = models.CharField(max_length=100)
    caste = models.IntegerField(choices=CASTE)
    gender = models.IntegerField(choices=GENDERS)
    father_name = models.CharField(max_length=100)
    spouse_name = models.CharField(
        max_length=100, blank=True, null=False, default='')
    spouse_aadhar = models.CharField(max_length=12,
                                     validators=[
                                         RegexValidator(
                                             regex=r'^[0-9]{12}$',
                                             message='Spouse\'s Aadhar number not valid.')],
                                     blank=True, null=False, default='')
    pan_number = models.CharField(max_length=10,
                                  validators=[RegexValidator(regex=r'^[A-Z]{5}[0-9]{4}[A-Z]{1}$',
                                                             message='Pan number not valid.')])
    aadhar_no = models.CharField(max_length=12,
                                 validators=[RegexValidator(regex=r'^[0-9]{12}$',
                                                            message='Aadhar number not valid.')])
    birth_date = models.DateField()
    phone = models.CharField(max_length=13, unique=True,
                             validators=[RegexValidator(regex=r'^(?:\+?91)?[789]\d{9,10}$',
                                                        message='Phone number not valid.')])
    email = models.EmailField(unique=True)
    address = models.TextField()
    password = models.CharField(max_length=128)
    uid = models.CharField(max_length=40, unique=True, blank=True)
    is_login = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    verified_by = models.ForeignKey(
        Admin, on_delete=models.CASCADE, null=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        from django.core.exceptions import ValidationError
        if (self.spouse_name != '' and self.spouse_aadhar == '') or (
                self.spouse_name == '' and self.spouse_aadhar != ''):
            raise ValidationError('Incomplete spouse details.')

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
