from rest_framework import serializers
from .models import CustomUser, UserHost, Profile, UserProfileImage, UserHostPassportImage, SocialUser
from travel_tours.serializers import TourSerializer, FavoriteSerializer, CommentSerializer


class SocialUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialUser
        fields = "__all__"


class UserProfileImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfileImage
        fields = '__all__'


class UserHostPassportImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserHostPassportImage
        fields = '__all__'


class UserHostSerializer(serializers.ModelSerializer):
    tours = TourSerializer(many=True, read_only=True)
    host_passport_images = UserHostPassportImageSerializer(many=True, read_only=True)

    class Meta:
        model = UserHost
        fields = (
            "id",
            "is_host",
            "telephone",
            "user_id",
            "host_passport_images",
            "tours",
        )


class ProfileSerializer(serializers.ModelSerializer):
    socials = SocialUserSerializer(many=True, read_only=True)
    profile_images = UserProfileImageSerializer(many=True, read_only=True)

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
            "profile_images",
            "socials",
        )


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    comments = CommentSerializer(many=True)
    favorites = FavoriteSerializer(many=True)
    host = UserHostSerializer()

    class Meta:
        model = CustomUser
        fields = [
            'id',
            'email',
            'date_joined',
            'profile',
            'favorites',
            'comments',
            'host'
        ]
