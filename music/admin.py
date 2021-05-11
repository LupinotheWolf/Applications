from django.contrib import admin
from .models import *

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    pass

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_filter = ['year']

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('surname', 'name')
    fields = [('surname', 'name'), 'albums']
