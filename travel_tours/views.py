from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, parser_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework import status
from .models import (
    Tour,
    TourImage
)
from .serializers import (
    TourSerializer,
    TourImageSerializer
)


@csrf_exempt
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
@parser_classes([JSONParser])
def tour_view(request):
    """
    Get all tours and post tour.
    """
    if request.method == "GET":
        tours = Tour.objects.all()
        serializer = TourSerializer(tours, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TourSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
@parser_classes([JSONParser])
def tour_detail_view(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    tour = get_object_or_404(Tour, pk=pk)

    if request.method == 'GET':
        serializer = TourSerializer(tour)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TourSerializer(tour, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        tour.delete()
        return Response({'message': "Deleted successfully!"}, status=status.HTTP_204_NO_CONTENT)

@csrf_exempt
@api_view(['POST', ])
# @permission_classes([IsAuthenticated, ])
@parser_classes([MultiPartParser, FormParser])
def tour_images(request):
    serializer = TourImageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "File has been uploaded successfully"}, status=200)
    else:
        return Response({"message": "File has NOT been uploaded successfully"}, status=400)

