from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import (
    get_user_model, authenticate, login, logout)
from .models import Movie, Genre
from .forms import (
    TelegramContactForm, MovieCreateForm,
    SignUpForm, SignInForm)
from .utils import send_notif_telegram
from django.http import HttpResponse

User = get_user_model()


def index(request):
    movies = Movie.objects.order_by('-date_add').all()
    genre_count = Genre.objects.count()
    movie_year = Movie.objects.order_by('year').all()
    sum_rating = 0
    for movie in movies:
        sum_rating += movie.rating
    avg_rating = sum_rating / len(movies)

    return render(request, 'movies/index.html', {'movies': movies,
                                                 'genre_count': genre_count,
                                                 'last_year': movie_year.last().year,
                                                 'first_year': movie_year.first().year,
                                                 'avg_rating': avg_rating,
                                                 })

def users_list(request):
    users = User.objects.filter(is_staff=True).all()
    return render(request, 'movies/users.html', {'users': users})

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
        return render(request, 'movies/request-a-qoute.html', {'form': form})


@login_required
def movies_add(request):
    if request.method == 'POST':
        form = MovieCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movies:movies_list_index')
    else:
        form = MovieCreateForm()
        return render(request, 'movies/movie_add.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if User.objects.filter(username=username).exists():
            form = SignUpForm()
            return render(request,
                          'auth/signup.html',
                          {'error': 'Пользователь с таким логином уже существует',
                           'form': form})

        if password != confirm_password:
            form = SignUpForm()
            return render(request,
                          'auth/signup.html',
                          {'error': 'Пароли не совпадают',
                           'form': form})
        
        if form.is_valid():
            User.objects.create_user(username=username, password=password)
            return redirect('movies:signin')
        return render(request, 'auth/signup.html', {'form': form})
    form = SignUpForm()
    return render(request, 'auth/signup.html', {'form': form})


def signin(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        
        if not User.objects.filter(username=username).exists:
            form = SignInForm()
            return render(request,
                          'auth/signin.html',
                          {'error': 'Пользователь с таким логином не существует',
                           'form': form})
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect('movies:movies_list_index')
        
        form = SignInForm()
        return render(request, 'auth/signin.html', {'form': form,
                                                    'error': 'Ошибка логина'})

    form = SignInForm()
    return render(request, 'auth/signin.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('movies:signin')
