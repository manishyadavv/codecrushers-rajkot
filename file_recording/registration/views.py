from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from file_recording.constants.response_obj import ReturnObj
from file_recording.registration.serializer import RegistrationWriteSerializer
# Create your views here.


@api_view(['POST'])
@parser_classes((JSONParser,))
def user_application(request):
    serializer = RegistrationWriteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return_obj = ReturnObj().ret(201)
        return_obj['content']['result']['application'] = serializer.data
    else:
        return_obj = ReturnObj().ret(200)
        return_obj['content']['result']['error'] = serializer.errors
    return Response(data=return_obj['content'], status=return_obj['status'])
