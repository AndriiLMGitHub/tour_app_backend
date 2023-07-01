from django.contrib import admin
from .models import Tour, TourImage, Favorite, City, Comment


# ---- Travel tours models admin ----
class TourAdmin(admin.ModelAdmin):
    search_fields = ('name', 'city',)


admin.site.register(Tour, TourAdmin)
admin.site.register(TourImage)
admin.site.register(Favorite)
admin.site.register(City)
admin.site.register(Comment)
