from django.urls import path

from apps.watchlist.api.views import (
    # movie_list,
    # movie_detail,
    MovieListAV,
    MovieDetailAV
)


urlpatterns = [
    path('list/', MovieListAV.as_view(), name='movie-list'),
    path('<int:pk>/', MovieDetailAV.as_view(), name='movie-detail'),

    # path('list/', movie_list, name='movie-list'),
    # path('<int:pk>/', movie_detail, name='movie-detail'),
]
