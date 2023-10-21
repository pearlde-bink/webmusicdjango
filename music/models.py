from django.db import models
# from django.contrib.auth.models import User
from os import name

# Create your models here.
class Music(models.Model):
    title = models.CharField(max_length=500)
    artist = models.CharField(max_length=500)
    # album = models.ForeignKey('Album', on_delete=models.SET_NULL, null=True, blank=True)
    audio_file = models.FileField(upload_to='musics/')
    cover_image = models.ImageField(upload_to='music_image/')
    lyrics = models.TextField(blank=True, null=True)
    vocabulary = models.TextField(blank=True, null=True)
    example = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.title
    
    class META:
        ordering = ['title']
    
# class Album(models.Model):
#     name = models.CharField(max_length=400)
    
# class Vocab(models.Model): 
#     eng = models.CharField(max_length=100)
#     meaning = models.CharField(max_length=200, blank=True, null=True)
    
#     def __str__(self): return self.eng
    
#     class META:
#         ordering = ['eng']
    