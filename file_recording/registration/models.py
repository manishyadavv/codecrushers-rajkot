from django.db import models

from file_recording.schemes.models import Flat
from file_recording.user.models import User
# Create your models here.


class Registration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             null=False, blank=False, related_name='applications')
    flat = models.ForeignKey(Flat, on_delete=models.CASCADE,
                             null=False, blank=False, related_name='registerations')
    is_verified = models.BooleanField(default=False)
    is_valid = models.NullBooleanField(default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
