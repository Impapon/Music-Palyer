from django.db import models
from django.contrib.auth.models import User

class Song(models.Model):
    song_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=2000)
    singer=models.CharField(max_length=2000)
    tags=models.CharField(max_length=2000)
    image=models.ImageField(upload_to='images')
    song=models.FileField(upload_to='images')
    movie=models.CharField(max_length=200,default="")
    credit=models.CharField(max_length=100000,default="")

    def __str__(self):
        return self.name

class Watchlater(models.Model):
    watch_id = models.AutoField(primary_key=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    video_id=models.CharField(max_length=1000000,default="")