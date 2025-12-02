from django.shortcuts import render
from django.contrib.auth import get_user_model
from .models import Movie

User = get_user_model()


def movies_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies.html', {'movies': movies})

def users_list(request):
    users = User.objects.filter(is_staff=True).all()
    return render(request, 'users.html', {'users': users})
