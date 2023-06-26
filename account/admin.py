from django.contrib import admin
from .models import Profile, CustomUser, UserHost, UserProfileImage, UserHostPassportImage

# ---- Account models admin ----
admin.site.register(CustomUser)
admin.site.register(UserHost)
admin.site.register(Profile)
admin.site.register(UserProfileImage)
admin.site.register(UserHostPassportImage)