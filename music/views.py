from django.shortcuts import render
from .models import *

def index(request):
    site_hits = request.session.get('sit_hits', 1)
    request.session['site_hits'] = site_hits + 1

    all_songs = Song.objects.all()
    all_artists = Artist.objects.all()

    context = {
        'all_songs': all_songs,
        'all_artists': all_artists,
        'site_hits': site_hits,
    }

    return render(request, 'musicindex.html', context = context)
