from django.db import models
from django.core.validators import (
    MaxValueValidator, MinValueValidator)

GENRE_MAX_LENGTH = 100

AUTHOR_MAX_LENGTH = 200
MOVIE_TITLE_MAX_LENGTH = 150
MOVIE_DESC_MAX_LENGTH = 1500
MIN_RATING = 0
MAX_RATING = 10


class Genre(models.Model):
    """
    Модель описывающая жанр фильма.
    """
    name = models.CharField(max_length=GENRE_MAX_LENGTH,
                            verbose_name='Название жанра')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        ordering = ('name',)


class Movie(models.Model):
    """
    Модель описывающая фильм.
    """
    genre = models.ForeignKey(
        Genre, on_delete=models.CASCADE,
        related_name='movies', verbose_name='Жанр')

    author = models.CharField(verbose_name='Автор(ы) фильма',
                              max_length=AUTHOR_MAX_LENGTH)

    title = models.CharField(max_length=MOVIE_TITLE_MAX_LENGTH,
                             verbose_name='Название фильма')
    description = models.TextField(max_length=MOVIE_DESC_MAX_LENGTH,
                                   verbose_name='Описание фильма')
    rating = models.FloatField(
        verbose_name='Рейтинг фильма',
        validators=[
            MinValueValidator(MIN_RATING),
            MaxValueValidator(MAX_RATING)])
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Дата создания')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
        ordering = ('-created_at',)
