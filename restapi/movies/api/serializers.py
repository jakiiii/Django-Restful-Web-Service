from rest_framework import serializers

from movies.models import Movie


def name_length(value):
    if len(value) < 2:
        raise serializers.ValidationError("Name is too short")


class MovieSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(validators=[name_length])
    description = serializers.CharField()
    active = serializers.BooleanField()

    class Meta:
        model = Movie
        fields = [
            'id',
            'name',
            'description',
            'active',
        ]

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance

    def validate(self, attrs):
        if attrs['name'] == attrs['description']:
            raise serializers.ValidationError("Title and Description should be diffrent!")
        return attrs

    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name is too short")
    #     return value
