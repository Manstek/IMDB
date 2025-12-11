from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('cinema.urls')),

    path('admin/', admin.site.urls),
]
