from django.urls import path

from .views import (
    toy_list,
    toy_detail
)

urlpatterns = [
    path('', toy_list, name='api_toys_list'),
    path('<int:pk>/', toy_detail, name='api_toy_detail'),
]
