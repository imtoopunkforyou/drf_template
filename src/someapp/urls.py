from django.urls import path
from . import views

urlpatterns = [
    path(
        'album/',
        views.album,
        name='album'
    ),
    path(
        'album/<int:pk>/',
        views.single_album,
        name='single_album'
    ),
    path(
        'track/',
        views.track,
        name='track'
    ),
    path(
        'track/<int:pk>/',
        views.single_track,
        name='single_track'
    ),
]
