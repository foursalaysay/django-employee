
from django.db import models

class Employee(models.Model):
    employee_id = models.CharField(max_length=10)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=32)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    hire_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
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