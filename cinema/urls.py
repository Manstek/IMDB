from django.urls import path, include, reverse_lazy
from .views import (
    ContactTemplateView, PrivacyPolicyTemplateView, GenreListView,
    MovieListView, MovieDetailView, MovieCreateView, MovieUpdateView,
    MovieDeleteView, CreateView)
from django.contrib.auth.forms import UserCreationForm


app_name = 'cinema'

urlpatterns = [
    path('', MovieListView.as_view(), name='movies'),
    path('genres/', GenreListView.as_view(), name='genres'),
    path('movies/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),
    path('movie-add/', MovieCreateView.as_view(), name='movie-add'),
    path('movie-edit/<int:pk>/', MovieUpdateView.as_view(), name='movie-edit'),
    path('movie-delete/<int:pk>/',
         MovieDeleteView.as_view(),
         name='movie-delete'),

    path('auth/', include('django.contrib.auth.urls')),
    path('auth/registration/',
         CreateView.as_view(
             template_name='registration/registration.html',
             form_class=UserCreationForm,
             success_url=reverse_lazy('cinema:movies')
         ),
         name='registration'),

    path('contact/', ContactTemplateView.as_view(), name='contact'),
    path('policy/', PrivacyPolicyTemplateView.as_view(), name='privacy'),
]
