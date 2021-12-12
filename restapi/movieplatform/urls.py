from django.urls import path
from movieplatform.views import (
    StreamPlatformAV,
    StreamPlatformDetailAV,
    WatchListAV,
    WatchListDetailAV,
    ReviewCreate,
    ReviewList,
    ReviewDetail,
)

app_name = 'movie-platform'


urlpatterns = [
    path('watch-list/', WatchListAV.as_view(), name='watchlist-api'),
    path('watch-list/<int:id>/', WatchListDetailAV.as_view(), name='watchlist-detail-api'),
    path('stream/', StreamPlatformAV.as_view(), name='stream-api'),
    path('stream/<int:id>/', StreamPlatformDetailAV.as_view(), name='stream-detail-api'),

    # path('review/', ReviewList.as_view(), name='review-list-api'),
    # path('review/<int:id>/', ReviewDetail.as_view(), name='review-detail-api'),

    path('watch-list/<int:id>/review-create/', ReviewCreate.as_view(), name='stream-review-create-api'),
    path('stream/<int:id>/review/', ReviewList.as_view(), name='stream-review-list-api'),
    path('stream/review/<int:id>/', ReviewDetail.as_view(), name='stream-review-detail-api'),
]
