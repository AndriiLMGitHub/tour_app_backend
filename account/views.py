from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser, FileUploadParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, parser_classes, permission_classes
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from .serializers import (
    UserSerializer,
    ProfileSerializer,
    UserHostSerializer,
    UserProfileImageSerializer,
    UserHostPassportImageSerializer,
    SocialUserSerializer,
)
from .models import CustomUser, Profile, UserHost, SocialUser


@csrf_exempt
@api_view(['GET', ])
@parser_classes([JSONParser])
@permission_classes([IsAuthenticated])
def users_with_profiles_view(request):
    if request.method == "GET":
        users = CustomUser.objects.all()
        serializer = UserSerializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@csrf_exempt
@api_view(['GET'])
@parser_classes([JSONParser])
@permission_classes([IsAuthenticated])
def user_view(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


@csrf_exempt
@api_view(['GET', 'PUT', 'POST'])
@parser_classes([JSONParser, FileUploadParser])
@permission_classes([IsAuthenticated])
def profile_edit_view(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    if request.method == 'GET':
        serializer = ProfileSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProfileSerializer(profile, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['PUT', ])
@parser_classes([JSONParser])
@permission_classes([IsAuthenticated])
def social_edit(request, pk):
    social = get_object_or_404(SocialUser, pk=pk)
    if request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = SocialUserSerializer(social, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['POST', ])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def profile_image(request):
    if request.method == 'POST':
        serializer = UserProfileImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['POST', ])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def host_image(request):
    if request.method == 'POST':
        serializer = UserHostPassportImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET', 'POST'])
@parser_classes([JSONParser])
@permission_classes([IsAuthenticated])
def host(request):
    if request.method == "GET":
        hosts = UserHost.objects.all()
        serializer = UserHostSerializer(hosts, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = UserHostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['PUT', ])
@parser_classes([JSONParser, ])
@permission_classes([IsAuthenticated])
def host_edit(request, pk):
    host = get_object_or_404(UserHost, pk=pk)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserHostSerializer(host, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
