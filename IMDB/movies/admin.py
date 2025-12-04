from django.contrib import admin
from .models import Movie, Genre


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name',)
    ordering = ('name', )
    list_editable = ('name',)
    list_display_links = None

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'year', 'author', 'rating', 'date_add')
    search_fields = ('genre', 'year', 'rating',)
    ordering = ('-year',)
    
