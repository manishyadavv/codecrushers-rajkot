from django.db import models

from file_recording.schemes.models import Flat
from file_recording.schemes.models import Scheme
from file_recording.user.models import User
# Create your models here.


class DrawResult(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=False, blank=False)
    flat = models.ForeignKey(
        Flat, on_delete=models.CASCADE, null=False, blank=False)
    scheme = models.ForeignKey(
        Scheme, on_delete=models.CASCADE, null=False, blank=False)
    waiting_number = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
