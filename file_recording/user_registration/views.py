from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from file_recording.constants.response_obj import ReturnObj
from file_recording.user_registration.serializer import UserRegistrationSerializer


@api_view(['POST'])
@parser_classes((JSONParser,))
def register_user(request):
    data = request.data
    user = UserRegistrationSerializer(data=data)
    if user.is_valid():
        user.save()
        return_obj = ReturnObj().ret(201)
        return_obj['content']['result'] = user.data
    else:
        print(user.errors)
        return_obj = ReturnObj().ret(400)
        return_obj['content']['result'] = user.errors

    return Response(data=return_obj['content'], status=return_obj['status'])
