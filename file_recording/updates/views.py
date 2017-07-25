from rest_framework.response import Response
from rest_framework.views import APIView

from .models import notification
from .serializers import notificationSerializer


# List of all the notifications or ceate a new one
# notifications/


class notificationList(APIView):
    def get(self, request):
        notifications = notification.objects.all()
        serializer = notificationSerializer(notifications, many=True)
        return Response(serializer.data)

    def post(self):
        pass
