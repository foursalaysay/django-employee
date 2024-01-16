from django.db import models
from django.contrib.auth.models import AbstractUser
from django.shortcuts import get_object_or_404

class Employee(AbstractUser):
    employee_id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    contact = models.CharField(max_length=15)
    address = models.TextField()
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=128)
    groups = models.ManyToManyField('auth.Group', related_name='employee_groups', blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name='employee_permissions', blank=True)

    def __str__(self):
        return f"{self.username} - {self.employee_id}"

    @classmethod
    def get_employee_by_username_password(cls, username, password):
        try:
            employee = cls.objects.get(username=username, password=password)
            return employee
        except cls.DoesNotExist:
            return None

class SalaryInfo(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
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
        return cls.objects.filter(employee__employee_id=employee_id).first()

class Document(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/')  # 'upload_to' defines the upload directory

    def __str__(self):
        return self.title
