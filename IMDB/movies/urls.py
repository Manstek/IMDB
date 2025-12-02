from django.urls import path
from .views import movies_list, users_list


urlpatterns = [
    path('', movies_list),
    path('users/', users_list),
]
