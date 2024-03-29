from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class Employee(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    contact = models.CharField(max_length=15)
    address = models.TextField()
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=128)
    groups = models.ManyToManyField('auth.Group', related_name='employee_groups', blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name='employee_permissions', blank=True)

    def __str__(self):
        return f"{self.username}"
    

    @classmethod
    def get_employee_by_username_password(cls, username, password):
        try:
            employee = cls.objects.get(username=username, password=password)
            return employee
        except cls.DoesNotExist:
            return None

class SalaryInfo(models.Model):
    username = models.CharField(max_length=255)
    employmentType = models.CharField(max_length=100, default='regular')
    basic_salary = models.DecimalField(max_digits=20, decimal_places=2)
    sss = models.DecimalField(max_digits=20, decimal_places=2)
    philhealth = models.DecimalField(max_digits=20, decimal_places=2)
    pagibig = models.DecimalField(max_digits=20, decimal_places=2)
    tax = models.DecimalField(max_digits=20, decimal_places=2)
    total_deduction = models.DecimalField(max_digits=20, decimal_places=2)
    netpay = models.DecimalField(max_digits=20, decimal_places=2)
    date_saved = models.DateTimeField(auto_now_add=True)


class Payment(models.Model):
    username = models.CharField(max_length=255)
    salary_value = models.DecimalField(max_digits=20, decimal_places=2)
    pay_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    
    
