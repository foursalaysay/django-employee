
from django.db import models
from django.contrib.auth.models import AbstractUser

class Employee(AbstractUser):
    employee_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    contact_number = models.CharField(max_length=15)
    address = models.TextField()
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=128)  # For simplicity, you might want to use Django's built-in password hashing instead

    def __str__(self):
        return self.username
    
    @classmethod
    def get_employee_by_username_password(cls, username, password):
        try:
            employee = cls.objects.get(username=username, password=password)
            return employee
        except cls.DoesNotExist:
            return None

class SalaryInfo(models.Model):
    employee_id = models.CharField(max_length=10)
    basic_salary = models.DecimalField(max_digits=20, decimal_places=2)
    sss = models.DecimalField(max_digits=20, decimal_places=2)
    philhealth = models.DecimalField(max_digits=20, decimal_places=2)
    pagibig = models.DecimalField(max_digits=20, decimal_places=2)
    tax = models.DecimalField(max_digits=20, decimal_places=2)
    total_deduction = models.DecimalField(max_digits=20, decimal_places=2)
    netpay = models.DecimalField(max_digits=20, decimal_places=2)
    month = models.CharField(max_length=100)

    @classmethod
    def get_salary_info_by_employee_id(cls, employee_id):
        return cls.objects.filter(employee_id=employee_id).first()


class Document(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/')  # 'upload_to' defines the upload directory

    def __str__(self):
        return self.title