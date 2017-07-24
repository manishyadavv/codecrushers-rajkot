import hashlib

from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    phone = models.CharField(max_length=10, unique=True)
    email = models.CharField(max_length=50, unique=True)
    address = models.TextField()
    password = models.CharField(max_length=128)
    uid = models.CharField(max_length=40, unique=True)
    is_login = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        self.uid = hashlib.sha1(str(self.id)).hexdigest()
        super(User, self).save(*args, **kwargs)


class LoginLog(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=False, blank=False)
    login_time = models.DateTimeField(blank=False, null=False)
    logout_time = models.DateTimeField(default=None)
    auto_logout = models.BooleanField(default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
