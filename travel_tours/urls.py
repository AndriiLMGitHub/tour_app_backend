from django.urls import path
from . import views

urlpatterns = [
    path('tours/', views.tour_view),
    path('tours/<int:pk>', views.tour_detail_view),
    path('tours/images/upload/', views.tour_images)
]