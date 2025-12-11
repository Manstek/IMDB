from django.views.generic import (
    TemplateView, ListView, DetailView, CreateView,
    UpdateView, DeleteView)
from .models import Genre, Movie
from .forms import MovieForm
from django.urls import reverse_lazy


class ContactTemplateView(TemplateView):
    template_name = 'cinema/contact.html'


class PrivacyPolicyTemplateView(TemplateView):
    template_name = 'cinema/policy.html'


class GenreListView(ListView):
    model = Genre
    template_name = 'cinema/genre_list.html'
    context_object_name = 'genre_list'


class MovieListView(ListView):
    model = Movie
    template_name = 'cinema/movie_list.html'
    context_object_name = 'movie_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movies_count'] = context['movie_list'].count()
        return context


class MovieDetailView(DetailView):
    model = Movie
    template_name = 'cinema/movie_card.html'
    context_object_name = 'movie'


class MovieCreateView(CreateView):
    model = Movie
    template_name = 'cinema/movie_add.html'
    form_class = MovieForm
    success_url = reverse_lazy("cinema:movies")


class MovieUpdateView(UpdateView):
    model = Movie
    template_name = 'cinema/movie_add.html'
    form_class = MovieForm
    success_url = reverse_lazy("cinema:movies")


class MovieDeleteView(DeleteView):
    model = Movie
    template_name = 'cinema/movie_add.html'
    success_url = reverse_lazy("cinema:movies")
