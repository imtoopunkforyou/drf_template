import tabnanny
from django.contrib import admin
from . import models

class TrackInline(admin.TabularInline):
    model = models.Track
    extra = 0

@admin.register(models.Album)
class AlbumAdmin(admin.ModelAdmin):
    inlines = (TrackInline, )
    list_display = ('name', 'artist', 'poster')
    search_fields = ('name', 'artist')
    
    
@admin.register(models.Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ('album', 'order', 'title', 'duration')
    search_fields = ('album', 'title')