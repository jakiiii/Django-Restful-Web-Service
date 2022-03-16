from django.urls import path

from apps.watchlist.api.views import (
    # movie_list,
    # movie_detail,
    WatchListListAV,
    WatchListDetailAV,
    StreamPlatformListAV,
    StreamPlatformDetailAV,
    ReviewCreateAPI,
    ReviewListAPI,
    ReviewDetailAPI
)


urlpatterns = [
    path('watchlist/', WatchListListAV.as_view(), name='watchlist-api'),
    path('watchlist/<int:pk>/', WatchListDetailAV.as_view(), name='watchlist-detail-api'),

    path('stream/', StreamPlatformListAV.as_view(), name='stream-api'),
    path('stream/<int:pk>/', StreamPlatformDetailAV.as_view(), name='stream-detail-api'),
    # path('<int:pk>/', movie_detail, name='movie-detail'),

    path('review/', ReviewListAPI.as_view(), name='review-api'),
    path('review/<int:pk>/', ReviewDetailAPI.as_view(), name='review-detail-api'),

    path('stream/<int:pk>/review/create/', ReviewCreateAPI.as_view(), name='stream-review-create-api'),
    path('stream/<int:pk>/review/', ReviewListAPI.as_view(), name='stream-review-list-api'),
    path('stream/review/<int:pk>/', ReviewDetailAPI.as_view(), name='stream-review-detail-api'),
]
