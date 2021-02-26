from django.urls import path

from drones.api.v2.views import ApiRootVersion2
from drones.api.views import (
    DroneCategoryList,
    DroneCategoryDetail,
    DroneList,
    DroneDetail,
    PilotList,
    PilotDetail,
    CompetitionList,
    CompetitionDetail,
)


urlpatterns = [
    path('vehicle-categories/', DroneCategoryList.as_view(), name=DroneCategoryList.name),
    path('vehicle-categories/<int:pk>/', DroneCategoryDetail.as_view(), name=DroneCategoryDetail.name),
    path('vehicles/', DroneList.as_view(), name=DroneList.name),
    path('vehicles/<int:pk>/', DroneDetail.as_view(), name=DroneDetail.name),
    path('pilots/', PilotList.as_view(), name=PilotList.name),
    path('pilots/<int:pk>/', PilotDetail.as_view(), name=PilotDetail.name),
    path('competitions/', CompetitionList.as_view(), name=CompetitionList.name),
    path('competitions/<int:pk>/', CompetitionDetail.as_view(), name=CompetitionDetail.name),
    path('', ApiRootVersion2.as_view(), name=ApiRootVersion2.name)
]
