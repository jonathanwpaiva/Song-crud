from django.urls import path
from . import views
from .views import detail_view
from .views import update_view
from .views import delete_view


app_name = "music"

urlpatterns = [
    path("",views.homepage),
    path("adicionar/", views.create_view, name="add"),
    path("listar/", views.list_view, name="list"),     
    path('listar/<id>', detail_view ),
    path('<id>/update', update_view ), 
    path('<id>/delete', delete_view ),
    path('update-delete', views.update_delete_view, name="list"),
   
]