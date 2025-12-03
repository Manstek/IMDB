from django.db import models
from django.core.validators import (MaxValueValidator, MinValueValidator)
import datetime

MAX_YEAR = datetime.datetime.now().year
MIN_YEAR = 1888


class Movie(models.Model):
    """Класс, описывающий модель данных - Фильм."""

    title = models.CharField(max_length=200)

    description = models.CharField(max_length=1000, blank=False)

    author = models.CharField(max_length=100)

    date_add = models.DateField(auto_now_add=True)

    genre = models.CharField(choices=[('Comedy', 'Комедия'), ('Drama', 'Драма'), ('War', 'Боевик')],
                             max_length=25)


    year = models.IntegerField(validators=[MinValueValidator(MIN_YEAR),
                                           MaxValueValidator(MAX_YEAR)])

    rating = models.FloatField()

    def __str__(self):
        return f"{self.author}, {self.year}: {self.title}"
    
    class Meta:
        ordering = ['-rating',]
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
