from django.contrib import admin

from file_recording.document.models import Document
from file_recording.document.models import DocumentType
# Register your models here.
admin.site.register(DocumentType)
admin.site.register(Document)
