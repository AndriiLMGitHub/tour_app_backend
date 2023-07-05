from django.db import models
from ckeditor.fields import RichTextField


class Page(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    text = RichTextField()

    def __str__(self):
        return self.title[0:10]


class PageImage(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name="page_images")
    image = models.FileField(upload_to="pages/images/")

    def __str__(self):
        return f'Image - {self.page}'


