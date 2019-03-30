from django.shortcuts import render

# Create your views here.
from .models import Artist, Song

from .forms import ArtistForm


def artist_list(request):
    artists = Artist.objects.all()
    return render(request, 'tunr/artist_list.html', {'artists': artists})


def artist_show(request, pk):
    artist = Artist.objects.get(id=pk)
    return render(request, 'tunr/artist_show.html', {'artist': artist})

def create_artist(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST)
        if form.is_valid():
            artist = form.save()
            return redirect('artist_detail', pk=artist.pk)  
        else:
          form = ArtistForm()

    return render(request, 'tunr/artist_form.html', {'form': form})


def song_list(request):
    songs = Song.objects.all()
    return render(request, 'tunr/song_list.html', {'songs': songs})


def song_detail(request, pk):
    song = Song.objects.get(id=pk)
    return render(request, 'tunr/song_detail.html', {'song': song})
