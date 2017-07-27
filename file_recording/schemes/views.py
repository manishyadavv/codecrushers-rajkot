from datetime import datetime

from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from file_recording.constants.response_obj import ReturnObj
from file_recording.schemes.models import Scheme
from file_recording.schemes.serializers import SchemeSerializer
# Create your views here.


@api_view(['GET'])
@parser_classes((JSONParser,))
def get_schemes(request):
    if request.query_params.get('admin'):
        schemes = Scheme.objects.all()
        serializer = SchemeSerializer(schemes, many=True)
    elif request.query_params.get('scheme_slug'):
        scheme_slug = request.query_params.get('scheme_slug')
        try:
            scheme = Scheme.objects.get(slug=scheme_slug)
        except Scheme.DoesNotExist:
            return_obj = ReturnObj().ret(404)
            return_obj['content']['result']['message'] = 'Invalid slug.'
            return Response(data=return_obj['content'], status=return_obj['status'])
        serializer = SchemeSerializer(scheme)

    else:
        schemes = Scheme.objects.filter(
            start_date__lte=datetime.now(), end_date__gte=datetime.now())
        serializer = SchemeSerializer(schemes, many=True)

    return_obj = ReturnObj().ret(200)
    return_obj['content']['result']['schemes'] = serializer.data
    return Response(data=return_obj['content'], status=return_obj['status'])


@api_view(['POST'])
@parser_classes((JSONParser,))
def create_scheme(request):
    pass
#     scheme = request.data.get('scheme')
#     flats = request.data.get('flats')
#     schemeserializer = SchemeSerializer(data=request.data)
#     if not schemeserializer.is_valid():
#         return_obj = ReturnObj().ret(400)
#         return_obj['content']['result']['message'] = schemeserializer.errors
#         return Response(data=return_obj['content'], status=return_obj['status'])
#     for flat in flats:
#         flat_serializer = FlatSerializer(data=flat)
#         if not flat_serializer.is_valid():
#             return_obj = ReturnObj().ret(400)
#             return_obj['content']['result']['message'] = flat_serializer.errors
#             return Response(data=return_obj['content'], status=return_obj['status'])
#
#     scheme = schemeserializer.save()
#     for flat in flats:
#         flat_type, _ = FlatType.objects.get_or_create(
#             name=flat.pop('flat_type'))
#         Flat(**flat, scheme=scheme, flat_type=flat_type).save()
#     schemeserializer.is_valid()
#     print(schemeserializer.errors)
#     schemeserializer.save()
#     return_obj = ReturnObj().ret(201)
#     return_obj['content']['result']['scheme'] = schemeserializer.data
#     return Response(data=return_obj['content'], status=return_obj['status'])
