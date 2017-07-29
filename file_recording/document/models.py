from autoslug.fields import AutoSlugField
from django.db import models

from file_recording.user.models import User


class DocumentType(models.Model):
    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='name')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Document(models.Model):
    user = models.ForeignKey(User, related_name='documents',
                             on_delete=models.CASCADE, null=False, blank=False)
    document = models.TextField(null=False, blank=False)
    mime_type = models.CharField(max_length=100)
    document_type = models.ForeignKey(
        DocumentType, on_delete=models.CASCADE, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
