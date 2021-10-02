from rest_framework import serializers
from rest_framework.reverse import reverse as api_reverse
from status.models import Status
from accounts.api.serializers import UserPublicSerializers


class StatusSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)
    user = UserPublicSerializers(read_only=True)

    class Meta:
        model = Status
        fields = (
            'uri',
            'id',
            'user',
            'content',
            'image'
        )
        read_only_fields = ['user']

    def get_uri(self, obj):
        return api_reverse('api-status-detail', kwargs={'id': obj.id}, request=self.context.get('request'))
