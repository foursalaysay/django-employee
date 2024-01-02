from django.db import models

# Create your models here.

# models.py inside your Django app

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=20)
    address = models.CharField(max_length=255)

