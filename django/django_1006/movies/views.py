from django.shortcuts import render, redirect
from .forms import MovieForm
from .models import Movie

# Create your views here.

def index(request):
    movies = Movie.objects.all()
    context = {
        'movies' : movies
    }
    return render(request, 'movies/index.html', context=context)

def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    context = {'movie' : movie,}
    return render(request, 'movies/detail.html', context=context)

def create(request):
    print(request.method)
    if request.method == 'POST':
        movie_form = MovieForm(request.POST)
        if movie_form.is_valid():
            movie_form.save()
            return redirect('movies:index')
    else:
        movie_form = MovieForm()
    context = {'movie_form' : movie_form,}
    return render(request, 'movies/create.html', context=context)        

def update(request, pk):
    movie = Movie.objects.get(pk=pk)
    print(request.method)
    if request.method == 'POST':
        movie_form = MovieForm(request.POST, instance=movie)
        if movie_form.is_valid():
            movie_form.save()
            return redirect('movies:detail', pk)
    else:
        movie_form = MovieForm(instance=movie)
    context = {'movie_form' : movie_form,}
    return render(request, 'movies/update.html', context=context)     

def delete(request, pk):
    movie = Movie.objects.get(pk=pk)
    print(request.method)
    if request.method == 'POST':
        movie.delete()
        return redirect('movies:index')
    else:
        return redirect('movies:detail', pk)