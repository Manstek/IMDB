from django import forms
from .models import Movie


class TelegramContactForm(forms.Form):
    """Форма для обратной связи."""
    name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()


class MovieCreateForm(forms.ModelForm):
    """Форма для добавления фильма на сайт пользователями."""

    class Meta:
        model = Movie
        fields = ('title', 'description', 'year', 'author', 'rating')


class SignUpForm(forms.Form):
    """Форма для регистрации."""
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
    confirm_password = forms.CharField(max_length=100)


class SignInForm(forms.Form):
    """Форма для регистрации."""
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)