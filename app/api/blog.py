from django.views.decorators.http import require_http_methods

from util import common


@require_http_methods(['GET'])
def getHandle(request):
    return common.makeResponseJson()


@require_http_methods(['GET'])
def getListHandle(request):
    return common.makeResponseJson()


@require_http_methods(['POST'])
def addHandle(request):
    return common.makeResponseJson()


@require_http_methods(['PUT'])
def editHandle(request):
    return common.makeResponseJson()


@require_http_methods(['DELETE'])
def deleteHandle(request):
    return common.makeResponseJson()
