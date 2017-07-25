from django.db import models

# Create your models here.


class notification(models.Model):
    scheme = models.CharField(max_length=500)
    validity = models.CharField(max_length=50)

    def __str__(self):
        return self.scheme
