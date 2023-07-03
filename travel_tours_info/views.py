from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, parser_classes, permission_classes
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import Page, PageImage
from .serializers import PageSerializer, PageImageSerializer


@csrf_exempt
@api_view(['GET', 'POST'])
@parser_classes([JSONParser, ])
def page_api_view(request):
    if request.method == "GET":
        pages = Page.objects.all()
        serializer = PageSerializer(pages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = PageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
@parser_classes([JSONParser, ])
def page_detail_api_view(request, pk):
    page = get_object_or_404(Page, pk=pk)
    if request.method == "GET":
        serializer = PageSerializer(page)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = PageSerializer(page, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        page.delete()
        return Response({"message": "Page has been deleted successfully!"}, status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
@api_view(['POST', ])
@parser_classes([MultiPartParser, FormParser])
def page_image_upload_view(request):
    serializer = PageImageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "File has been uploaded successfully"}, status=200)
    else:
        return Response({"message": "File has NOT been uploaded successfully"}, status=400)
