from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, parser_classes, permission_classes
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from .serializers import UserSerializer, ProfileSerializer, UserHostSerializer
from .models import CustomUser, Profile, UserHost


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
@api_view(['GET', 'PUT'])
@parser_classes([JSONParser])
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
@api_view(['PUT', 'GET'])
@parser_classes([JSONParser])
@permission_classes([IsAuthenticated])
def host(request):
    if request.method == "GET":
        hosts = UserHost.objects.all()
        serializer = UserHostSerializer(hosts, many=True)
        return Response(serializer.data)


@csrf_exempt
@api_view(['PUT', ])
@parser_classes([JSONParser])
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
