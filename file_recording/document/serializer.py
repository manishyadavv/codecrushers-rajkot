# -*- coding: utf-8 -*-
from rest_framework import serializers

from file_recording.document.models import Document
from file_recording.document.models import DocumentType


class DocumentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentType
        exclude = ('created_at', 'updated_at')


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        exclude = ('id',)
