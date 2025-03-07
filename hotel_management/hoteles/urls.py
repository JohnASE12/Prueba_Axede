from django.urls import path
from .views import search_rooms

urlpatterns = [
    path('buscar/', search_rooms, name='search_rooms'),
]
