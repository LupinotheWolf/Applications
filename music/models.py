from django.db import models
from django.urls import reverse

class Genre(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

class Song(models.Model):
    title = models.CharField(max_length = 30, help_text = 'Enter the name of the song')
    track_number = models.PositiveIntegerField()
    genre = models.ManyToManyField(Genre, help_text = 'Choose a genre for this song', blank = True)

    class Meta:
        ordering = ['-title']

    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])
    def __str__(self):
        return self.title

class Album(models.Model):
    name = models.CharField(max_length = 30)
    songs = models.ManyToManyField(Song, help_text = 'Select songs that belong to this album')
    year = models.PositiveIntegerField(blank = True, null = True)
    cover_photo = models.ImageField(upload_to = 'images/album_cover_photos/', blank = True, null = True)

    def __str__(self):
        return self.name


class Artist(models.Model):
    surname = models.CharField(max_length = 30)
    name = models.CharField(max_length = 30)
    albums = models.ManyToManyField(Album)

    def __str__(self):
        return f'{self.surname}, {self.name}'
    def get_absolute_url(self):
        return reverse('artist-detail', args=[str(self.id)])
