from django.db import models
from datetime import datetime

class Artiste(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    age=models.IntegerField()
    
    def __str__(self):
        return self.first_name + " " + self.last_name
    
class Song(models.Model):
    Artiste=models.ForeignKey(Artiste, on_delete=models.CASCADE)
    title=models.CharField(max_length=30)
    date_released=models.DateField(default=datetime.today)
    likes=models.DateField(max_length=30)
    # artiste_id=models.CharField(max_length=400)
    
    def __str__(self):
        return self.Artiste.first_name + " " + self.Artiste.last_name
    
class Lyric(models.Model):
    Artiste=models.ForeignKey(Artiste, on_delete=models.CASCADE)
    content=models.CharField(max_length=30)
    song_id=models.CharField(max_length=30)
    
    def __str__(self):
        return self.Artiste.first_name + " " + self.Artiste.last_name + " " + self.class_name
    
    
# Create your models here.
