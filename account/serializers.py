from rest_framework import serializers
from .models import CustomUser, UserHost, Profile, UserProfileImage, UserHostPassportImage
from travel_tours.serializers import TourSerializer, FavoriteSerializer, CommentSerializer


class UserProfileImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfileImage
        fields = '__all__'


class UserHostPassportImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserHostPassportImage
        fields = '__all__'


class UserHostSerializer(serializers.ModelSerializer):
    host_passport_images = UserHostPassportImageSerializer(many=True, read_only=True)
    class Meta:
        model = UserHost
        fields = (
            "id",
            "is_host",
            "telephone",
            "user_id",
            "host_passport_images",
        )


class ProfileSerializer(serializers.ModelSerializer):
    profile_image = UserProfileImageSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = (
            "id",
            "sex",
            "name",
            "date_birth",
            "address",
            "bio",
            "city",
            "is_verified",
            "user",
            "profile_image",
        )


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
