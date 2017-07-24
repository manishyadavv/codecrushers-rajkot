from rest_framework import serializers

from file_recording.user_registration.models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('id', 'uid', 'created_at', 'updated_at')
