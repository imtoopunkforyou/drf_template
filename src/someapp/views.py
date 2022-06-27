from drf_yasg.utils import swagger_auto_schema
from .models import Album, Track
from . import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_201_CREATED, HTTP_204_NO_CONTENT


@swagger_auto_schema(method='post', request_body=serializers.RequestAlbumSerializer)
@api_view(['GET', 'POST'])
def album(request):
    """Описание"""
    try:
        queryset = Album.objects.all()
    except Album.DoesNotExist:
        return Response(status=HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serialize = serializers.AlbumSerializer(queryset, many=True)
        return Response(data=serialize.data, status=HTTP_200_OK)

    if request.method == 'POST':
        data = {
            'name': request.data.get('name'),
            'artist': request.data.get('artist'),
            'poster': request.data.get('poster')
        }
        serialize = serializers.RequestAlbumSerializer(data=data)
        if serialize.is_valid(raise_exception=True):
            serialize.save()
            return Response(serialize.data, status=HTTP_201_CREATED)


@swagger_auto_schema(method='delete', request_body=serializers.RequestAlbumSerializer)
@api_view(['GET', 'DELETE'])
def single_album(request, pk):
    """Описание"""
    try:
        queryset = Album.objects.get(pk=pk)
    except Album.DoesNotExist:
        return Response(status=HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        queryset = Album.objects.filter(pk=pk)
        serialize = serializers.AlbumSerializer(queryset, many=True)
        return Response(data=serialize.data, status=HTTP_200_OK)

    if request.method == 'DELETE':
        queryset.delete()
        return Response(status=HTTP_204_NO_CONTENT)


@swagger_auto_schema(method='post', request_body=serializers.RequestTrackSerializer)
@api_view(['GET', 'POST'])
def track(request):
    """Описание"""
    try:
        queryset = Track.objects.all()
    except Track.DoesNotExist:
        return Response(status=HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serialize = serializers.TrackSerializer(queryset, many=True)
        return Response(data=serialize.data, status=HTTP_200_OK)

    if request.method == 'POST':
        data = {
            'album': int(request.data.get('album')),
            'order': request.data.get('order'),
            'title': request.data.get('title'),
            'duration': int(request.data.get('duration'))
        }
        serialize = serializers.RequestTrackSerializer(data=data)
        if serialize.is_valid(raise_exception=True):
            serialize.save()
            return Response(serialize.data, status=HTTP_201_CREATED)


@swagger_auto_schema(method='delete', request_body=serializers.RequestTrackSerializer)
@api_view(['GET', 'DELETE'])
def single_track(request, pk):
    """Описание"""
    try:
        queryset = Track.objects.get(pk=pk)
    except Track.DoesNotExist:
        return Response(status=HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        queryset = Track.objects.filter(pk=pk)
        serialize = serializers.TrackSerializer(queryset, many=True)
        return Response(data=serialize.data, status=HTTP_200_OK)

    if request.method == 'DELETE':
        queryset.delete()
        return Response(status=HTTP_204_NO_CONTENT)
