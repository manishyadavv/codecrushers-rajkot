from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from file_recording.constants.response_obj import ReturnObj
from file_recording.document.models import Document
from file_recording.document.models import DocumentType
from file_recording.document.serializer import DocumentSerializer
from file_recording.document.serializer import DocumentTypeSerializer
from file_recording.user.models import User


@api_view(['GET'])
@parser_classes((JSONParser,))
def doc_types(request):
    types = DocumentType.objects.all()
    serializer = DocumentTypeSerializer(types, many=True)
    return_obj = ReturnObj().ret(200)
    return_obj['content']['result']['document_types'] = serializer.data
    return Response(data=return_obj['content'], status=return_obj['status'])


@api_view(['POST'])
@parser_classes((JSONParser,))
def upload_file(request):
    n = len(request.data)
    for i in range(n):
        request.data[i]['user'] = User.objects.get(
            uid=request.data[i]['user']).id
    serializer = DocumentSerializer(data=request.data, many=True)
    if serializer.is_valid():
        serializer.save()
        return_obj = ReturnObj().ret(201)
        return_obj['content']['result']['message'] = 'File uploaded'
    else:
        return_obj = ReturnObj().ret(400)
        return_obj['content']['result']['errors'] = serializer.errors
    return Response(data=return_obj['content'], status=return_obj['status'])


@api_view(['GET'])
@parser_classes((JSONParser,))
def get_file(request):
    uid = request.query_params['uid']
    if request.query_params.get('doc_type'):
        documents = Document.objects.get(
            user__uid=uid, document_type__slug=request.query_params['doc_type'])
    else:
        documents = Document.objects.filter(user__uid=uid)
    docs = []
    for doc in documents:
        docs.append({'doc_string': doc.document,
                     'mime_type': doc.mime_type,
                     'document_type': DocumentTypeSerializer(
                         doc.document_type).data})
    return_obj = ReturnObj().ret(200)
    return_obj['content']['result']['documents'] = docs
    return Response(data=return_obj['content'], status=return_obj['status'])
