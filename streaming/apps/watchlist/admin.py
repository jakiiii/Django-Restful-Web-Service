from django.contrib import admin
from apps.watchlist.models import WatchList, StreamPlatform, Review


@admin.register(WatchList)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'active']


@admin.register(StreamPlatform)
class StreamPlatformAdmin(admin.ModelAdmin):
    list_display = ['name', 'website']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['watchlist', 'ratting', 'created_at']
