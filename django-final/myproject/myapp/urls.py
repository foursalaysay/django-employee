from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("user/home", views.userhome, name="user-home"),
    path("user/profile-management", views.profile_management_view, name="profile_management_view")
]
