from django.db import models
from autoslug import AutoSlugField
from file_recording.user.models import User

# Create your models here.

class DocumentType(models.Model):
	name = models.TextField(max_length=50)
	slug = AutoSlugField(populate_from='name')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)


class Document(models.Model):
	document_type = models.ForeignKey('DocumentType',on_delete=models.CASCADE)
	document_desc = models.CharField(max_length=100)
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	document = models.FileField()
	created_at = models.DateTimeField(auto_now_add=True)
	update_at = models.DateTimeField(auto_now=True
