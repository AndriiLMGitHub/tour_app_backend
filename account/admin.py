from django.contrib import admin
from .models import Profile, CustomUser, UserHost

# ---- Account models admin ----
admin.site.register(CustomUser)
admin.site.register(UserHost)
admin.site.register(Profile)