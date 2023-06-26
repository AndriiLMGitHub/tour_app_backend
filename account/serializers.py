from rest_framework import serializers
from .models import CustomUser, UserHost, Profile
from travel_tours.serializers import TourSerializer, FavoriteSerializer, CommentSerializer


class UserHostSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserHost
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    comments = CommentSerializer(many=True)
    tours = TourSerializer(many=True)
    favorites = FavoriteSerializer(many=True)
    host = UserHostSerializer()

    class Meta:
        model = CustomUser
        fields = [
            'id',
            'email',
            'profile',
            'tours',
            'favorites',
            'comments',
            'host'
        ]
