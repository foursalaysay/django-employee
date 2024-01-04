from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("user/home", views.userhome, name="user-home")
]
