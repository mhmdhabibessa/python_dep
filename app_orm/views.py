from django.shortcuts import render,redirect
from .models import Movie,Actor
from django.contrib import messages

def index(request):
    data = {
        'dark': 'black',
        "movies" : Movie.objects.all(),
        "actors" : Actor.objects.all(),
    }
    return render(request,"index.html",data)

def form_movie(request):

    return render(request,"form.html")

def create_movie(request):
    errors = Movie.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key,value in errors.items():
            messages.error(request,value,extra_tags=key)
        # print(messages.get_messages(error))
        return redirect('/form-movie')
    else:
        Movie.objects.create(
            title=request.POST['title'],
            description = request.POST['description'],
            duration=request.POST['duration'],
            image_url = request.POST['image_url'],
            release_date= '2024-05-16 07:21:59.247030',
            actors = Actor.objects.get(id=1)
            )
        return redirect('/')
