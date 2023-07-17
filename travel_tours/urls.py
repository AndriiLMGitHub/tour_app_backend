from django.urls import path
from . import views

urlpatterns = [
    path('tours/types/', views.TourTypeAPIView.as_view()),
    path('tours/', views.get_all_tours),
    path('tours/all/', views.GetTours.as_view()),
    path('tours/create/', views.tour_view),
    path('tours/edit/<int:pk>/', views.tour_detail_edit_view),
    path('tours/<int:pk>/', views.tour_detail),
    path('tours/images/upload/', views.tour_images),
    path('tours/comments/all/', views.comment_all_view),
    path('tours/comments/all/list/', views.CommentsAll.as_view()),
    path('tours/comment/create/', views.comment_create),
    path('tours/comment/<int:pk>/', views.comment_view),
    path('tours/cities/', views.cites_all_view),
    path('tours/cities/all/', views.CitiesAll.as_view()),
    path('tours/cities/<int:pk>/', views.city_view),
    path('tours/add_to_favorites/', views.add_to_favorites),
    path('tours/delete_favorite/<int:pk>/', views.delete_favorite),

    path('tours/search/', views.SearchTourAPIView.as_view())
]
