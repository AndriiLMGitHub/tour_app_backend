from django.urls import path
from . import views


urlpatterns = [
    # All Users
    path('', views.users_with_profiles_view),
    # One user
    path('<int:pk>/', views.user_view),
    # One Profile of User
    path('profile/<int:pk>/', views.profile_edit_view),
    path('profile/social/<int:pk>/', views.social_edit),
    path('profile/image/upload/', views.profile_image),
    # All hosts
    path('profile/host/', views.host),
    # One host
    path('profile/host/<int:pk>/', views.host_edit),
    path('profile/host/image/upload/', views.host_image),
]