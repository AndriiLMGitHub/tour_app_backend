from django.db import models


class Page(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title[0:10]


class PageImage(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name="page_images")
    image = models.FileField(upload_to="pages/images/")


