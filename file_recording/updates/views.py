from datetime import datetime

from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from file_recording.constants.response_obj import ReturnObj
from file_recording.updates.models import Notification
from file_recording.updates.serializers import NotificationSerializer


# List of all the notifications or create a new one
# notifications/

@api_view(['GET', 'POST'])
@parser_classes((JSONParser,))
def notification(request):
    if request.method == 'GET':
        notifications = Notification.objects.filter(
            start_date__gte=datetime.now(), end_date__lte=datetime.now())
        serializer = NotificationSerializer(notifications, many=True)
        return_obj = ReturnObj().ret(200)
        return_obj['content']['result']['notifications'] = serializer.data
        return Response(data=return_obj['content'], status=return_obj['status'])
    elif request.method == 'POST':
        serializer = NotificationSerializer(data=request.data)
        if serializer.is_valid():
            return_obj = ReturnObj().ret(201)
            return_obj['content']['result']['notification'] = serializer.data
            return Response(data=return_obj['content'], status=return_obj['status'])
        else:
            return_obj = ReturnObj().ret(400)
            return_obj['content']['result']['errors'] = serializer.errors
            return Response(data=return_obj['content'], status=return_obj['status'])
