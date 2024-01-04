from django.db import models

# Create your models here.

from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100)
    password
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    hire_date = models.DateField()

    # You can add more fields as needed for your Employee model

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

