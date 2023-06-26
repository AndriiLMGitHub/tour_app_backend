from django.db import models
from django.conf import settings


class City(models.Model):
    city_name = models.CharField(max_length=120)
    city_image = models.FileField(upload_to='city/images/')

    def __str__(self):
        return f'The city is {self.city_name}'

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cites'


class Tour(models.Model):
    TYPES = (
        ('Backpaking', 'Backpaking'),
        ('Weekend', 'Weekend'),
        ('Adventure', 'Adventure'),
        ('Solo', 'Solo'),
    )
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tours')
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='tours')
    name = models.CharField(max_length=120)
    type = models.CharField(max_length=120, choices=TYPES)
    date_start = models.DateTimeField()
    date_finish = models.DateTimeField()
    languages = models.CharField(max_length=120)
    longitude = models.CharField(max_length=120)
    latitude = models.CharField(max_length=120)
    address = models.CharField(max_length=120)
    price = models.PositiveIntegerField()
    is_active = models.BooleanField(default=False)
    rating = models.BigIntegerField(default=0)

    def __str__(self):
        return f'The name of tour is {self.name}'


class TourImage(models.Model):
    tour_id = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='images')
    tour_images = models.FileField(upload_to='tours/images/', null=True, blank=True)

    def __str__(self):
        return f'Image of tour {self.tour_id}'


class Comment(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    tour_id = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment of {self.tour_id}'


class Favorite(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='favorites')
    tours = models.ManyToManyField(Tour, related_name='favorites')

    def __str__(self):
        return f'Tours of user {self.user_id}'
