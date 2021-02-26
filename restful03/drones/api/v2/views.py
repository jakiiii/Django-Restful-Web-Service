from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse

from drones.api import views


class ApiRootVersion2(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'drone-category': reverse(views.DroneCategoryList.name, request=request),
            'drones': reverse(views.DroneList.name, request=request),
            'pilots': reverse(views.PilotList.name, request=request),
            'competitions': reverse(views.CompetitionList.name, request=request)
        })
