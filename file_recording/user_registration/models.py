from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=100, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=5000)
