from django.contrib import admin
from apps.watchlist.models import WatchList, StreamPlatform


@admin.register(WatchList)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'active']


@admin.register(StreamPlatform)
class StreamPlatformAdmin(admin.ModelAdmin):
    list_display = ['name', 'website']
