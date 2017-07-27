# -*- coding: utf-8 -*-
from rest_framework.serializers import ModelSerializer

from file_recording.registration.models import Registration


class RegistrationWriteSerializer(ModelSerializer):
    class Meta:
        model = Registration
        exclude = ('id',)
