from django.urls import path
from .views import (
    movies_list, users_list, contact, movies_add)

app_name = 'movies'


urlpatterns = [
    path('', movies_list, name='movies_list'),
    path('users/', users_list, name='user-admin-list'),
    path('contact/', contact, name='request-a-qoute-telegram'),
    path('movie-add/', movies_add, name='movie_add')
]
