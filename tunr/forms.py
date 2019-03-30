from django import forms
from .models import Artist, Song

class ArtistForm(form.ModelForm):
    class Meta:
        model = Artist
        