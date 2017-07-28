from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from file_recording.constants.response_obj import ReturnObj
from file_recording.employee.models import Admin
from file_recording.registration.models import Registration
from file_recording.registration.serializer import RegistrationReadSerializer
from file_recording.registration.serializer import RegistrationWriteSerializer
from file_recording.user.models import User
# Create your views here.


@api_view(['POST', 'GET'])
@parser_classes((JSONParser,))
def user_application(request):
    if request.method == 'POST':
        user = User.objects.get(uid=request.data['user'])
        request.data['user'] = user.id
        serializer = RegistrationWriteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return_obj = ReturnObj().ret(201)
            return_obj['content']['result']['application'] = serializer.data
        else:
            return_obj = ReturnObj().ret(200)
            return_obj['content']['result']['error'] = serializer.errors
    elif request.method == 'GET':
        uid = request.query_params.get('uid')
        user = User.objects.get(uid=uid)
        registrations = Registration.objects.filter(user=user)
        serializer = RegistrationReadSerializer(registrations, many=True)
        return_obj = ReturnObj().ret(200)
        return_obj['content']['result']['registrations'] = serializer.data
    return Response(data=return_obj['content'], status=return_obj['status'])


@api_view(['POST'])
@parser_classes((JSONParser,))
def validate(request):
    employee = Admin.objects.get(employee_id=request.data['employee_id'])
    application = Registration.objects.get(id=request.data['application_id'])
    application.verified_by = employee
    application.is_valid = request.data['is_valid']
    application.save()
    print('saved and verified')
