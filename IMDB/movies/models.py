from django.db import models


class Movie(models.Model):
    """Класс, описывающий модель данных - Фильм."""

    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    author = models.CharField(max_length=100)
    date_add = models.DateField(auto_now_add=True)


    year = models.IntegerField()

    rating = models.FloatField()

    def __str__(self):
        return f"{self.author}, {self.year}: {self.title}"