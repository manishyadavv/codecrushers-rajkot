# -*- coding: utf-8 -*-
from rest_framework.serializers import ModelSerializer

from file_recording.employee.models import Admin


class AdminSerializer(ModelSerializer):
    class Meta:
        model = Admin
        exclude = ('id', 'created_at', 'updated_at')
