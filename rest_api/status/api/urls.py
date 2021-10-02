from django.urls import path

from .view import (
    StatusListCreateView,
    StatusAPIDetailView,
)


urlpatterns = [
    path('', StatusListCreateView.as_view(), name=StatusListCreateView.name),
    path('<int:id>/', StatusAPIDetailView.as_view(), name='api-status-detail'),
]
