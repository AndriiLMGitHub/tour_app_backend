from django.contrib import admin
from .models import Tour, TourImage, Favorite, City, Comment

# ---- Travel tours models admin ----
admin.site.register(Tour)
admin.site.register(TourImage)
admin.site.register(Favorite)
admin.site.register(City)
admin.site.register(Comment)
