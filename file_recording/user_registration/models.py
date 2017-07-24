from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
