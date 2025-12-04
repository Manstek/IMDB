from django.db import models
from django.core.validators import (MaxValueValidator, MinValueValidator)
import datetime

MAX_YEAR = datetime.datetime.now().year
MIN_YEAR = 1888
MAX_RATING = 10
MIN_RATING = 0

class Genre(models.Model):
    """Класс, описывающий жанр фильма."""

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        ordering = ['name',]


class Movie(models.Model):
    """Класс, описывающий модель данных - Фильм."""

    genre = models.ForeignKey(Genre,
                              on_delete=models.SET_NULL,
                              related_name='movies',
                              null=True,
                              blank=True)

    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000, blank=False)
    author = models.CharField(max_length=100)
    year = models.IntegerField(validators=[MinValueValidator(MIN_YEAR),
                                           MaxValueValidator(MAX_YEAR)])
    rating = models.FloatField(validators=[MinValueValidator(MIN_RATING),
                                           MaxValueValidator(MAX_RATING)])

    date_add = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.author}, {self.year}: {self.title}"
    
    class Meta:
        ordering = ['-rating',]
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
