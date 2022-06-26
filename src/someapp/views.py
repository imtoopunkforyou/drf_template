from drf_yasg.utils import swagger_auto_schema
from .models import Album, Track
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND


@swagger_auto_schema(methods=['post', 'put', 'patch', 'delete'])
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def album(request):
    if request.method == 'GET':
        return Response('Hey, its get', status=HTTP_200_OK)
    if request.method == 'POST':
        return Response('Hey, its post', status=HTTP_200_OK)
    if request.method == 'PUT':
        return Response('Hey, its put', status=HTTP_200_OK)
    if request.method == 'PATCH':
        return Response('Hey, its patch', status=HTTP_200_OK)
    if request.method == 'DELETE':
        return Response('Hey, its delete', status=HTTP_200_OK)


@swagger_auto_schema(methods=['post', 'put', 'patch', 'delete'])
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def single_album(request, pk):
    if request.method == 'GET':
        return Response('Hey, its get', status=HTTP_200_OK)
    if request.method == 'POST':
        return Response('Hey, its post', status=HTTP_200_OK)
    if request.method == 'PUT':
        return Response('Hey, its put', status=HTTP_200_OK)
    if request.method == 'PATCH':
        return Response('Hey, its patch', status=HTTP_200_OK)
    if request.method == 'DELETE':
        return Response('Hey, its delete', status=HTTP_200_OK)


@swagger_auto_schema(methods=['post', 'put', 'patch', 'delete'])
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def track(request):
    if request.method == 'GET':
        return Response('Hey, its get', status=HTTP_200_OK)
    if request.method == 'POST':
        return Response('Hey, its post', status=HTTP_200_OK)
    if request.method == 'PUT':
        return Response('Hey, its put', status=HTTP_200_OK)
    if request.method == 'PATCH':
        return Response('Hey, its patch', status=HTTP_200_OK)
    if request.method == 'DELETE':
        return Response('Hey, its delete', status=HTTP_200_OK)


@swagger_auto_schema(methods=['post', 'put', 'patch', 'delete'])
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def single_track(request, pk):
    if request.method == 'GET':
        return Response('Hey, its get', status=HTTP_200_OK)
    if request.method == 'POST':
        return Response('Hey, its post', status=HTTP_200_OK)
    if request.method == 'PUT':
        return Response('Hey, its put', status=HTTP_200_OK)
    if request.method == 'PATCH':
        return Response('Hey, its patch', status=HTTP_200_OK)
    if request.method == 'DELETE':
        return Response('Hey, its delete', status=HTTP_200_OK)
