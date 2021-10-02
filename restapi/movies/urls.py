from django.urls import path
from .views import (
    movie_list,
    movie_detail,
)

app_name = "movie"


urlpatterns = [
    path('list/', movie_list, name='movie-list'),
    path('<int:pk>/', movie_detail, name='movie-detail'),
]
