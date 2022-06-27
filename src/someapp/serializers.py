from .models import Album, Track
from rest_framework import serializers


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id', 'name', 'artist', 'poster']
        read_only_fields = fields


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ['id', 'album', 'order',
                  'title', 'duration']
        read_only_fields = fields


class RequestAlbumSerializer(serializers.ModelSerializer):
    poster = serializers.CharField()

    class Meta:
        model = Album
        fields = ['name', 'artist', 'poster']


class RequestTrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ['album', 'order', 'title', 'duration']
