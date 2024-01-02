# admin.py inside your ems_app

from django.contrib import admin
from .models import User

admin.site.register(User)  # Register the User model in the Django admin
