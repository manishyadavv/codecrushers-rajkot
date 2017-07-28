# -*- coding: utf-8 -*-
from rest_framework.serializers import ModelSerializer

from file_recording.registration.models import Registration
from file_recording.schemes.models import Flat
from file_recording.schemes.models import Scheme
from file_recording.schemes.serializers import FlatTypeSerializer


class RegistrationSchemeSerializer(ModelSerializer):
    class Meta:
        model = Scheme
        exclude = ('id', 'created_at', 'updated_at')


class RegistrationFlatSerializer(ModelSerializer):
    flat_type = FlatTypeSerializer()
    scheme = RegistrationSchemeSerializer()

    class Meta:
        model = Flat
        fields = '__all__'


class RegistrationWriteSerializer(ModelSerializer):
    class Meta:
        model = Registration
        exclude = ('id',)


class RegistrationReadSerializer(ModelSerializer):
    flat = RegistrationFlatSerializer()

    class Meta:
        model = Registration
        exclude = ('id',)
