from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, parser_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework import status
from rest_framework import filters
from rest_framework import generics
from .models import (
    TourType,
    Tour,
    Comment,
    City,
    Favorite,
    Language
)
from .serializers import (
    TourTypeSerializer,
    TourSerializer,
    TourImageSerializer,
    CommentSerializer,
    CitySerializer,
    FavoriteSerializer,
    LanguageSerializer
)


@csrf_exempt
@api_view(['GET', ])
@parser_classes([JSONParser, ])
def get_all_tours(request):
    """
    Get all tours and post tour.
    """
    if request.method == "GET":
        tours = Tour.objects.all()
        serializer = TourSerializer(tours, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# With pagination and query parametr limit
class GetTours(generics.ListAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer


@csrf_exempt
@api_view(['POST', ])
@permission_classes([IsAuthenticated, ])
@parser_classes([JSONParser, ])
def tour_view(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TourSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET', ])
@parser_classes([JSONParser])
def tour_detail(request, pk):
    tour = get_object_or_404(Tour, pk=pk)
    if request.method == 'GET':
        serializer = TourSerializer(tour)
        total = 0
        if serializer.data['comments']:
            for r in serializer.data['comments']:
                total = total + r['rating']
            tour.total_rating = total / len(serializer.data['comments'])
            serializer = TourSerializer(tour)
        return Response(serializer.data, status=status.HTTP_200_OK)


@csrf_exempt
@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
@parser_classes([JSONParser])
def tour_detail_edit_view(request, pk):
    tour = get_object_or_404(Tour, pk=pk)
    if request.method == 'PUT':
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
@permission_classes([IsAuthenticated, ])
@parser_classes([MultiPartParser, FormParser])
def tour_images(request):
    serializer = TourImageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "File has been uploaded successfully"}, status=200)
    else:
        return Response({"message": "File has NOT been uploaded successfully"}, status=400)


@csrf_exempt
@api_view(['GET', ])
@parser_classes([JSONParser])
def comment_all_view(request):
    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@csrf_exempt
@api_view(['GET', ])
@parser_classes([JSONParser])
def comment_view(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    serializer = CommentSerializer(comment)
    return Response(serializer.data, status=status.HTTP_200_OK)


class CommentsAll(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


@csrf_exempt
@api_view(['POST', ])
@permission_classes([IsAuthenticated])
@parser_classes([JSONParser])
def comment_create(request):
    data = JSONParser().parse(request)
    serializer = CommentSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET', ])
@parser_classes([JSONParser])
def cites_all_view(request):
    comments = City.objects.all()
    serializer = CitySerializer(comments, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


class CitiesAll(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer


@csrf_exempt
@api_view(['GET', ])
@parser_classes([JSONParser])
def city_view(request, pk):
    city = get_object_or_404(City, pk=pk)
    serializer = CitySerializer(city)
    return Response(serializer.data, status=status.HTTP_200_OK)


@csrf_exempt
@api_view(['POST', ])
@permission_classes([IsAuthenticated])
@parser_classes([JSONParser])
def add_to_favorites(request):
    data = JSONParser().parse(request)
    serializer = FavoriteSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['DELETE', ])
@permission_classes([IsAuthenticated])
@parser_classes([JSONParser])
def delete_favorite(request, pk):
    favorite = get_object_or_404(Favorite, pk=pk)
    if request.method == "DELETE":
        favorite.delete()
        return Response({"message": "Favorite has been deleted successfully!"}, status=status.HTTP_204_NO_CONTENT)


class SearchTourAPIView(generics.ListCreateAPIView):
    search_fields = ['price', 'total_rating', 'created_at', 'type__type', 'name', 'languages']
    queryset = Tour.objects.all()
    serializer_class = TourSerializer

    filter_backends = [filters.SearchFilter, ]


class TourTypeAPIView(generics.ListAPIView):
    queryset = TourType.objects.all()
    serializer_class = TourTypeSerializer


class LanguageAPIView(generics.ListAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
