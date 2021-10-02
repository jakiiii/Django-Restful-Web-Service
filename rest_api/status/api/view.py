from rest_framework import generics, mixins, permissions

from status.models import Status
from .serializers import StatusSerializer


class StatusListCreateView(generics.ListCreateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    name = 'status-list'


class StatusAPIDetailView(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.RetrieveAPIView):
    serializer_class = StatusSerializer
    queryset = Status.objects.all()
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
