from django.db import models

from file_recording.settings import fs
from file_recording.user_registration.models import User


class FileUpload(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User)
    datafile = models.FileField(storage=fs)
