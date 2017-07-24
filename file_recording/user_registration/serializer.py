from rest_framework import serializers

from file_recording.user_registration.models import Profile


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = ('id',)
