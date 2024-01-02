# urls.py inside your ems_app

from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup')
]
