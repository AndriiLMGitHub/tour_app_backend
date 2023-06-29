from django.urls import path
from . import views

urlpatterns = [
    path('page/', views.page_api_view),
    path('page/<int:pk>', views.page_detail_api_view),
    path('page/image/upload/', views.page_image_upload_view),
]