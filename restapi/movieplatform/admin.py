from django.contrib import admin
from movieplatform.models import StreamPlatform, WatchList, Reviews


@admin.register(StreamPlatform)
class StreamPlatformAdmin(admin.ModelAdmin):
    list_display = ['name', 'website']


@admin.register(WatchList)
class WatchListAdmin(admin.ModelAdmin):
    list_display = ['title', 'platform', 'active']


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ['watchlist', 'ratting', 'active', 'created']
