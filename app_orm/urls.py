from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),	   
    path('form-movie', views.form_movie),	   
    path('create_movie', views.create_movie),	   
]