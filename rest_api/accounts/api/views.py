from django.contrib.auth import get_user_model
from rest_framework import generics
from .serializers import UserRegistrationSerializers
from .permissions import AnonPermissionOnly

User = get_user_model()


class Registration(generics.CreateAPIView):
    permission_classes = [AnonPermissionOnly]
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializers

    def get_serializer_context(self, *args, **kwargs):
        return {'request': self.request}
