from django.shortcuts import render 
from django.shortcuts import (get_object_or_404, 
                              render, 
                              HttpResponseRedirect)   

from .models import song 
from .forms import MusicForm

def homepage(response):
    
    return render(response, "homepage.html")  

  
def create_view(request): 
    
    context ={} 
  
   
    form = MusicForm(request.POST or None) 
    if form.is_valid(): 
        form.save() 
        return HttpResponseRedirect("/") 
          
    context['form']= form 
    return render(request, "create_view.html", context) 

def list_view(request):    
    context ={} 
  
    
    context["dataset"] = song.objects.all() 
          
    return render(request, "list_view.html", context)

def update_delete_view(request):    
    context ={} 
  
    
    context["dataset"] = song.objects.all() 
          
    return render(request, "update-delete_view.html", context)

def detail_view(request, id): 
    
    context ={} 
  
    
    context["data"] = song.objects.get(id = id) 
          
    return render(request, "detail_view.html", context)

def update_view(request, id): 
    
    context ={} 
  
    
    obj = get_object_or_404(song, id = id) 
  
    
    form = MusicForm(request.POST or None, instance = obj) 
  
    
    if form.is_valid(): 
        form.save() 
        return HttpResponseRedirect("/") 
  
    
    context["form"] = form 
  
    return render(request, "update_view.html", context)  

def delete_view(request, id): 
   
    context ={} 
  
    
    obj = get_object_or_404(song, id = id) 
  
  
    if request.method =="POST": 
        
        obj.delete() 
       
        return HttpResponseRedirect("/") 
  
    return render(request, "delete_view.html", context) 





