# -*- coding: utf-8 -*-
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from file_recording.constants.response_obj import ReturnObj
from file_recording.employee.models import Admin
from file_recording.user.models import Session
from file_recording.user.models import User
from file_recording.user.serializer import UserReadSerializer
from file_recording.user.serializer import UserRegistrationSerializer
from file_recording.user.utils import user_login
from file_recording.user.utils import user_logout


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
    user = None
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return_obj = ReturnObj().ret(401)
        return_obj['content']['result']['message'] = 'No user with the given username exists.'
        return Response(data=return_obj['content'], status=return_obj['status'])

    if user:
        if user.password == password:
            if user.is_login:
                user_logout(user, user.session_set[0])
            session = user_login(user)
            return_obj = ReturnObj().ret(200)
            return_obj['content']['result']['message'] = 'Login Successful'
            return_obj['content']['result']['session_id'] = session.session_id
            return_obj['content']['result']['user_id'] = session.user.uid
        else:
            return_obj = ReturnObj().ret(401)
            return_obj['content']['result']['message'] = 'Incorrect Password.'

    return Response(data=return_obj['content'], status=return_obj['status'])


@api_view(['POST'])
@parser_classes((JSONParser,))
def logout_user(request):
    session_id = request.data.get('session_id')
    try:
        session = Session.objects.get(session_id=session_id, auto_logout=None)
    except Session.DoesNotExist:
        return_obj = ReturnObj().ret(404)
        return_obj['content']['result']['message'] = 'The given session does not exist.'
        return Response(data=return_obj['content'], status=return_obj['status'])
    if session.auto_logout is not None:
        return_obj = ReturnObj().ret(409)
        return_obj['content']['result']['message'] = 'The user is already logged out.'
        return Response(data=return_obj['content'], status=return_obj['status'])
    user_logout(session.user, session)
    return_obj = ReturnObj().ret(200)
    return_obj['content']['result']['message'] = 'Session successfully closed.'
    return Response(data=return_obj['content'], status=return_obj['status'])


@api_view(['GET'])
@parser_classes((JSONParser,))
def user_details(request):
    if request.query_params.get('session_id'):
        session_id = request.query_params.get('session_id')
        session = Session.objects.filter(session_id=session_id)
        if len(session) == 0:
            return_obj = ReturnObj().ret(404)
            return_obj['content']['result']['message'] = "Session id doesn't exist."
            return Response(data=return_obj['content'], status=return_obj['status'])
        else:
            serializer_data = UserReadSerializer(session[0].user).data
            return_obj = ReturnObj().ret(200)
            return_obj['content']['result']['user'] = serializer_data
            return Response(data=return_obj['content'], status=return_obj['status'])
    else:
        users = User.objects.all()
        serializer = UserReadSerializer(users, many=True)
        return_obj = ReturnObj().ret(200)
        return_obj['content']['result']['user'] = serializer.data
        return Response(data=return_obj['content'], status=return_obj['status'])


@api_view(['POST'])
@parser_classes((JSONParser,))
def validate_user(request):
    uid = request.data['uid']
    user = User.objects.get(uid=uid)
    employee = Admin.objects.get(email=request.data['email'])
    user.verified_by = employee
    user.is_verified = request.data['verified']
    user.save()
    return_obj = ReturnObj().ret(201)
    return_obj['content']['result']['message'] = 'User validation successful.'
    return Response(data=return_obj['content']['result'], status=return_obj['status'])
