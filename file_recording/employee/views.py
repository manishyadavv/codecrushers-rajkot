from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from file_recording.constants.response_obj import ReturnObj
from file_recording.employee.models import Admin
from file_recording.employee.serializer import AdminSerializer


@api_view(['POST'])
@parser_classes((JSONParser,))
def create_admin(request):
    serializer = AdminSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        print(serializer.errors)


@api_view(['POST'])
@parser_classes((JSONParser,))
def login_employee(request):
    email = request.data.get('email')
    password = request.data.get('password')
    employee = None
    try:
        employee = Admin.objects.get(email=email)
    except Admin.DoesNotExist:
        return_obj = ReturnObj().ret(401)
        return_obj['content']['result']['message'] = 'No user with the given username exists.'
        return Response(data=return_obj['content'], status=return_obj['status'])

    if employee:
        if employee.password == password:
            return_obj = ReturnObj().ret(200)
            return_obj['content']['result']['message'] = 'Login Successful'
        else:
            return_obj = ReturnObj().ret(401)
            return_obj['content']['result']['message'] = 'Incorrect Password.'

    return Response(data=return_obj['content'], status=return_obj['status'])

# Create your views here.
