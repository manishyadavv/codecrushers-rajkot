# -*- coding: utf-8 -*-
from rest_framework import serializers

from file_recording.user.models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('id', 'created_at', 'updated_at')


class UserReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('id',)
