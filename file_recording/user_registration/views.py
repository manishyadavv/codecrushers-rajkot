# -*- coding: utf-8 -*-
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from file_recording.constants.response_obj import ReturnObj
from file_recording.user_registration.models import User
from file_recording.user_registration.serializer import UserRegistrationSerializer
from file_recording.user_registration.utils import user_login


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


@api_view(['POST'])
@parser_classes((JSONParser,))
def login_user(request):
    email = request.data.get('email')
    password = request.data.get('password')
    user = User.objects.get(email=email)
    if not user:
        return_obj = ReturnObj().ret(401)
        return_obj['content']['result']['message'] = 'No user with the given username exists.'
    else:
        if user.password == password:
            user_login(user)
            return_obj = ReturnObj().ret(200)
            return_obj['content']['result']['message'] = 'Login Successful'
        else:
            return_obj = ReturnObj().ret(401)
            return_obj['content']['result']['message'] = 'Incorrect Password.'

    return Response(data=return_obj['content'], status=return_obj['status'])
