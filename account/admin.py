from django.contrib import admin
from .models import (
    Profile,
    CustomUser,
    UserHost,
    UserProfileImage,
    UserHostPassportImage,
    SocialUser
)


class CutomUserAdmin(admin.ModelAdmin):
    list_display = ["email", "date_joined", 'last_login', "is_active", "id"]
    list_filter = ["date_joined", "date_joined", "last_login", "is_active"]
    fields = [
        ("email", "password"),
        "date_joined",
        'last_login',
        (
            "is_active",
            "is_staff",
        ),
        "is_superuser",
        (
            "first_name",
            "last_name"
        ),
    ]
    search_fields = ['email', "id"]
    date_hierarchy = "date_joined"


class UserHostAdmin(admin.ModelAdmin):
    list_display = ["user_id", "is_host", 'rejected', "telephone"]
    fields = [
        "user_id",
        "telephone",
        "is_host",
        'rejected',
    ]
    search_fields = ["telephone", ]
    list_filter = ["is_host", 'rejected']


class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", ]
    search_fields = ["name", "city"]
    list_filter = ["sex", "city"]


class UserProfileImageAdmin(admin.ModelAdmin):
    search_fields = ["user_id", "avatar"]
    list_filter = ["user_id", ]
    raw_id_fields = ["user_id"]


class UserHostPassportImageAdmin(admin.ModelAdmin):
    list_filter = ["user_id", ]
    raw_id_fields = ["user_id"]


class SocialUserAdmin(admin.ModelAdmin):
    list_filter = ["user_profile_id", ]
    search_fields = ["type"]


# ---- Account models admin ----
admin.site.register(CustomUser, CutomUserAdmin)
admin.site.register(UserHost, UserHostAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(UserProfileImage, UserProfileImageAdmin)
admin.site.register(UserHostPassportImage, UserHostPassportImageAdmin)
admin.site.register(SocialUser, SocialUserAdmin)
