# -*- coding: utf-8 -*-
from rest_framework import serializers

from file_recording.result.models import DrawResult
from file_recording.schemes.serializers import FlatSerializer
from file_recording.schemes.serializers import SchemeWriteSerializer
from file_recording.user.serializer import UserReadSerializer


class DrawReadSerializer(serializers.ModelSerializer):
    scheme = SchemeWriteSerializer()
    flat = FlatSerializer()
    user = UserReadSerializer()

    class Meta:
        model = DrawResult
        exclude = ('id',)
