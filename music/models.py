from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.

#this class thingy creates individual tables
#the different variables are the different rows with the properties
#there can be functions in the class too
class Album(models.Model):
	artist=models.CharField(max_length=250)
	album_title=models.CharField(max_length=500)
	genre=models.CharField(max_length=100)
	album_logo=models.FileField()
	#specify the string representation of the Album object

	def get_absolute_url(self):
		return reverse('music:detail',kwargs={'pk':self.pk})


	def __str__(self):
		return self.album_title+' - '+self.artist

#another table
class Song(models.Model):
	#this makes a relation of the song with the album
	#if the album is delelted, so will each of the songs
	album=models.ForeignKey(Album,on_delete=models.CASCADE)
	file_type=models.CharField(max_length=10)
	song_title=models.CharField(max_length=250)
	is_favorite=models.BooleanField(default=False)

	def get_absolute_url(self):
		return reverse('music:index')

	def __str__(self):
		return self.song_title