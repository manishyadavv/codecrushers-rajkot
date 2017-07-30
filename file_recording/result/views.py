from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from file_recording.constants.response_obj import ReturnObj
from file_recording.registration.models import Registration
from file_recording.result.models import Allotment
from file_recording.result.models import DrawResult
from file_recording.result.serializer import DrawReadSerializer
# Create your views here.


@api_view(['GET'])
@parser_classes((JSONParser,))
def get_result(request):
    results = DrawResult.objects.filter(user__uid=request.data['uid'])
    serializer = DrawReadSerializer(results, many=True)
    return_obj = ReturnObj().ret(200)
    return_obj['content']['result']['results'] = serializer.data
    return Response(data=return_obj['content'], status=return_obj['status'])


@api_view(['POST'])
@parser_classes((JSONParser,))
def allocate_flat(request):
    application = Registration.objects.get(
        registration_id=request.data['registration_id'])
    allot = Allotment(user=application.user, flat=application.flat,
                      address=application.flat.scheme.location, amount_to_pay=application.flat.estimate_cost)
    allot.save()
    return_obj = ReturnObj().ret(201)
    return_obj['content']['result'] = {
        'allotment_id': allot.id,
        'message': 'Flat has been allocated.'
    }
    return Response(data=return_obj['content'], status=return_obj['status'])
