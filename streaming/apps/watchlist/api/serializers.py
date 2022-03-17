from rest_framework import serializers

from apps.watchlist.models import WatchList, StreamPlatform, Review


class ReviewSerializer(serializers.ModelSerializer):  # HyperlinkedModelSerializer):
    watchlist = serializers.StringRelatedField(many=False)
    reviewer = serializers.StringRelatedField(many=False, read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
        extra_kwargs = {
            'url': {'view_name': 'review-detail-api', 'lookup_field': 'pk'},
        }

    def create(self, validated_data):
        return Review.objects.create(**validated_data)


# class StreamPlatformListSerializer(serializers.ModelSerializer):
#     reviews = ReviewSerializer(many=True, read_only=True)
#     stream_url = serializers.HyperlinkedIdentityField(view_name='stream-detail-api')
#
#     class Meta:
#         model = StreamPlatform
#         fields = '__all__'


class WatchListSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    watchlist_url = serializers.HyperlinkedIdentityField(view_name='watchlist-detail-api')
    # platform = serializers.StringRelatedField(read_only=True)
    # platform = StreamPlatformListSerializer(read_only=True)
    platform = serializers.CharField(source='platform.name')

    class Meta:
        model = WatchList
        fields = '__all__'
        # fields = ('id', 'name', 'shortline', 'active')
        # exclude = ('active',)
        extra_kwargs = {
            'url': {'view_name': 'watchlist-detail-api', 'lookup_field': 'pk'},
        }

    def validate(self, attrs):
        if attrs['name'] == attrs['shortline']:
            raise serializers.ValidationError("Title and Description should be different!")
        return attrs

    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Name is too short!")
        return value


class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):  # (serializers.ModelSerializer):
    # nested serializer
    watchlist = WatchListSerializer(read_only=True, many=True)    # return all data
    # watchlist = serializers.StringRelatedField(many=True)     # return only string
    # watchlist = serializers.PrimaryKeyRelatedField(many=True, read_only=True)   # return primary key
    # watchlist = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='movie-detail')
    # stream_listing = serializers.HyperlinkedIdentityField(view_name='stream-detail-api')

    class Meta:
        model = StreamPlatform
        fields = '__all__'
        extra_kwargs = {
            'url': {'view_name': 'stream-detail-api', 'lookup_field': 'pk'},
        }


# def name_length(self, value):
#     if len(value) < 2:
#         raise serializers.ValidationError("Name is too short!")
#
#
# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     description = serializers.CharField()
#     active = serializers.BooleanField()
#
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
