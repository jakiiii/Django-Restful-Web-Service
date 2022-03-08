from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('movie/', include('apps.watchlist.urls')),
    path('api/movie/', include('apps.watchlist.api.urls')),
]
