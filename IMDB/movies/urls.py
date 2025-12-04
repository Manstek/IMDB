from django.urls import path
from .views import (
    index, users_list, contact, movies_add,
    signup, signin, logout_view)

app_name = 'movies'


urlpatterns = [
    path('', index, name='movies_list_index'),
    path('users/', users_list, name='user-admin-list'),
    path('contact/', contact, name='request-a-qoute-telegram'),
    path('movie-add/', movies_add, name='movie_add'),

    path('auth/signup/', signup, name='signup'),
    path('auth/signin/', signin, name='signin'),
    path('auth/logout/', logout_view, name='logout'),
]
