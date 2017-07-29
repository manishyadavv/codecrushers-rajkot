import hashlib
from datetime import datetime

from django.db import models


# Create your models here.

class Admin(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    created_by = models.ForeignKey(
        'Admin', on_delete=models.CASCADE, null=True, blank=False, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Session(models.Model):
    admin = models.ForeignKey(
        Admin, on_delete=models.CASCADE, null=False, blank=False)
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
