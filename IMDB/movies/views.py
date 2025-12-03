from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .models import Movie
from .forms import TelegramContactForm, MovieCreateForm
from .utils import send_notif_telegram
from django.http import HttpResponse


User = get_user_model()


def movies_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies.html', {'movies': movies})

def users_list(request):
    users = User.objects.filter(is_staff=True).all()
    return render(request, 'users.html', {'users': users})

def contact(request):
    if request.method == 'POST':
        form = TelegramContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            send_notif_telegram(name, last_name, email)
            return redirect('movies:movies_list')
    else:
        form = TelegramContactForm()
        return render(request, 'request-a-qoute.html', {'form': form})


def movies_add(request):
    if request.method == 'POST':
        form = MovieCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movies:movies_list')
    else:
        form = MovieCreateForm()
        return render(request, 'movie_add.html', {'form': form})
