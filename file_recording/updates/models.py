from django.db import models

# Create your models here.


class Notification(models.Model):
    message = models.CharField(max_length=500)
    url = models.URLField(null=True, default=None)
    end_date = models.DateField()
    start_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.message
