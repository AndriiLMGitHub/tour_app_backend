from rest_framework import serializers
from .models import (
    Tour,
    TourImage,
    Favorite,
    City,
    Comment
)


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

    class Meta:
        model = Tour
        fields = (
            'id',
            'user_id',
            'name',
            'type',
            'city',
            'date_start',
            'date_finish',
            'languages',
            'longitude',
            'latitude',
            'address',
            'price',
            'rating',
            'images',
            'comments'
        )


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'
