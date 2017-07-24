from django.db import models


class Profile(models.Model):
    Name = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    phone=models.CharField(max_length=10)
    Email=models.CharField(max_length=50)
    Address=models.CharField(max_length=5000)

