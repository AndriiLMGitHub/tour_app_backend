from rest_framework import serializers
from .models import (
    TourType,
    Tour,
    TourImage,
    Favorite,
    City,
    Comment
)


class TourTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourType
        fields = '__all__'


class TourImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourImage
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class TourSerializer(serializers.ModelSerializer):
    images = TourImageSerializer(read_only=True, many=True)
    comments = CommentSerializer(read_only=True, many=True)
    # type = serializers.CharField(read_only=True)

    class Meta:
        model = Tour
        fields = (
            'id',
            'user_id',
            'name',
            'type',
            'city',
            'description',
            'created_at',
            'date_start',
            'date_finish',
            'languages',
            'longitude',
            'latitude',
            'address',
            'price',
            'total_rating',
            'is_active',
            'images',
            'comments'
        )


class CitySerializer(serializers.ModelSerializer):
    tours = TourSerializer(many=True, read_only=True)

    class Meta:
        model = City
        fields = (
            "id",
            "city_name",
            "city_image",
            "tours"
        )


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'
