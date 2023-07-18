from django.contrib import admin
from .models import Page, PageImage


class PageAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_filter = ["created_at", "updated_at", ]


class PageImageAdmin(admin.ModelAdmin):
    search_fields = ("page__id", "page__title")
    raw_id_fields = ["page"]


# admin.site.register(Page, PageAdmin)
# admin.site.register(PageImage, PageImageAdmin)
