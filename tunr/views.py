from django.shortcuts import render

# Create your views here.
from .models import Artist, Song


def artist_list(request):
    artists = Artist.objects.all()
    return render(request, 'tunr/artist_list.html', {'artists': artists})
