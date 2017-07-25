from rest_framework import serializers

from .models import notification


class notificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = notification
        felds = '__all__'
