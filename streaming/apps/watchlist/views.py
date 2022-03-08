from django.shortcuts import render
from django.http import JsonResponse

from apps.watchlist.models import WatchList


def movie_list(request):
    movies = WatchList.objects.all()
    print(movies.values())
    data = {
        'movies': list(movies.values())
    }
    return JsonResponse(data)


def movie_detail(request, pk):
    movie = WatchList.objects.get(pk=pk)
    data = {
        'name': movie.name,
        'shortline': movie.shortline,
        'active': movie.active
    }
    return JsonResponse(data)
