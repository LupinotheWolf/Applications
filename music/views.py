from django.shortcuts import render
from .models import *

def index(request):
    all_songs = Song.objects.all()
    all_artists = Artist.objects.all()

    context = {
        'all_songs': all_songs,
        'all_artists': all_artists,
    }

    return render(request, 'musicindex.html', context = context)
