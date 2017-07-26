# -*- coding: utf-8 -*-
from rest_framework.serializers import ModelSerializer

from file_recording.schemes.models import Flat
from file_recording.schemes.models import FlatType
from file_recording.schemes.models import Scheme


class FlatTypeSerializer(ModelSerializer):
    class Meta:
        model = FlatType
        fields = '__all__'


class FlatSerializer(ModelSerializer):
    flat_type = FlatTypeSerializer(many=False)

    class Meta:
        model = Flat
        exclude = ('scheme',)


class SchemeSerializer(ModelSerializer):
    flats = FlatSerializer(many=True)

    class Meta:
        model = Scheme
        fields = '__all__'
