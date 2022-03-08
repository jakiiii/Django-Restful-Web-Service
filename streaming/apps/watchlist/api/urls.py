from django.urls import path

from apps.watchlist.api.views import (
    # movie_list,
    # movie_detail,
    WatchListListAV,
    WatchListDetailAV,
    StreamPlatformListAV,
    StreamPlatformDetailAV
)


urlpatterns = [
    path('list/', WatchListListAV.as_view(), name='movie-list'),
    path('<int:pk>/', WatchListDetailAV.as_view(), name='movie-detail'),
    path('stream/', StreamPlatformListAV.as_view(), name='stream-list'),
    path('stream/<int:pk>/', StreamPlatformDetailAV.as_view(), name='stream-detail'),
    # path('<int:pk>/', movie_detail, name='movie-detail'),
]
