from django.db import models
from django.contrib.auth.models import User

class Artist(models.Model):
    name = models.CharField(max_length=30)
    date_joined = models.DateField(auto_now_add=True)
  
    def __str__(self):
        return self.name
    
   

class song(models.Model):
    title = models.CharField(max_length=50)   
    duration = models.IntegerField()
    spotify_published = models.BooleanField()
    youtube_published = models.BooleanField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

   

   

#links usados para referencia
#https://www.geeksforgeeks.org/django-crud-create-retrieve-update-delete-function-based-views/
#https://books.agiliq.com/projects/django-admin-cookbook/en/latest/export.html
#https://www.youtube.com/watch?v=Dzuiy-JNi-E
