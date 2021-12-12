from rest_framework import serializers
from rest_framework.reverse import reverse as api_reverse

from movieplatform.models import StreamPlatform, WatchList, Reviews


class StringSerializer(serializers.StringRelatedField):

    def to_internal_value(self, data):
        return data


class ReviewsSerializer(serializers.ModelSerializer):
    watchlist = StringSerializer(many=False)

    class Meta:
        model = Reviews
        fields = '__all__'


class WatchListSerializer(serializers.HyperlinkedModelSerializer):
    platform = StringSerializer(many=False)
    reviews = ReviewsSerializer(many=True, read_only=True)

    class Meta:
        model = WatchList
        fields = '__all__'
        extra_kwargs = {
            'url': {'view_name': 'movie-platform:watchlist-detail-api', 'lookup_field': 'id'},
        }


class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)

    class Meta:
        model = StreamPlatform
        fields = '__all__'
        extra_kwargs = {
            'url': {'view_name': 'movie-platform:stream-detail-api', 'lookup_field': 'id'},
        }
