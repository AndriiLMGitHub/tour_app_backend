from rest_framework import serializers
from .models import Page, PageImage


class PageImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageImage
        fields = '__all__'


class PageSerializer(serializers.ModelSerializer):
    page_images = PageImageSerializer(many=True, read_only=True)

    class Meta:
        model = Page
        fields = (
            'id',
            'title',
            'created_at',
            'updated_at',
            'text',
            'page_images',
        )
