from rest_framework import serializers

from file_recording.updates.models import Notification


class NotificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notification
        exclude = ('id', 'created_at', 'updated_at')
