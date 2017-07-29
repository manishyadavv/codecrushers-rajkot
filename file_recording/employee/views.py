from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser

from file_recording.employee.models import Admin
from file_recording.employee.serializer import AdminSerializer


@api_view(['POST'])
@parser_classes((JSONParser,))
def create_admin(request):
    request.data['created_by'] = Admin.objects.get(
        employee_id=request.data['created_by']).id
    serializer = AdminSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        print(serializer.errors)

# Create your views here.
