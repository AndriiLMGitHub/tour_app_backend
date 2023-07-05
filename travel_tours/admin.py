from django.contrib import admin
from .models import Tour, TourImage, Favorite, City, Comment


# ---- Travel tours models admin ----
class TourAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "price",
        "created_at",
        "total_rating",
        "city"
    ]
    search_fields = (
        'name',
        'city',
        'price',
        'total_rating',
        "user_id__email"
    )
    list_filter = [
        "name",
        "price",
        "created_at",
        "total_rating",
        "city",
        "user_id"
    ]
    raw_id_fields = ["user_id"]


class TourImageAdmin(admin.ModelAdmin):
    list_display = ["tour_id", ]
    list_filter = [
        "tour_id__id",
        "tour_id__name",
        "tour_id__city",
        "tour_id__price",
        "tour_id__total_rating"
    ]
    search_fields = (
        "tour_id__id",
        "tour_id__name",
        "tour_id__city",
        "tour_id__price",
        "tour_id__total_rating"
    )
    raw_id_fields = ["tour_id"]


class FavoriteAdmin(admin.ModelAdmin):
    list_display = ["user_id", "tour_id"]
    list_filter = ["user_id__email", "tour_id__name"]
    search_fields = ("user_id__id", "tour_id__id")
    raw_id_fields = ["user_id", "tour"]


class CityAdmin(admin.ModelAdmin):
    search_fields = ('city_name',)
    list_filter = ["city_name", ]


class CommentAdmin(admin.ModelAdmin):
    list_display = ["user_id", "tour_id", "rating"]
    search_fields = (
        'rating',
        "tour_id__id",
        "tour_id__name",
        "tour_id__city",
        "tour_id__price",
        "tour_id__total_rating"
    )
    list_filter = [
        "created_at",
        "rating",
        "tour_id__id",
        "tour_id__name",
        "tour_id__city",
        "tour_id__price",
        "tour_id__total_rating"
    ]
    raw_id_fields = ["user_id", "tour_id"]


admin.site.register(Tour, TourAdmin)
admin.site.register(TourImage, TourImageAdmin)
admin.site.register(Favorite, FavoriteAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Comment, CommentAdmin)
