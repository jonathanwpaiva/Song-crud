
from django import forms 
from .models import song 
  
  

class MusicForm(forms.ModelForm): 
  
   
    class Meta: 
        
        model = song 
  
      
        fields = [ 
            "title", 
            "duration", 
            "spotify_published",
            "youtube_published",
            "artist",
        ] 

