from django.shortcuts import render
from .models import *

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def login_view(request):
    if request.method == 'POST':
        # If the form is submitted
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # If authentication is successful, log the user in
            login(request, user)
            return redirect('home')  # Replace 'home' with the name of your home URL pattern
        else:
            # If authentication fails, show an error message
            messages.error(request, 'Invalid username or password')

    # If the request is a GET request or authentication fails, render the login form
    return render(request, 'auth/login.html')


def register_view(request):
    if request.method == 'POST':
        # If the form is submitted
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        address = request.POST.get('address')
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if the username is already taken
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username is already taken')
            return redirect('register')  # Assuming 'register' is the name of your registration URL pattern

        # Create a new user
        user = User.objects.create_user(username=username, password=password, email=email, first_name=name)

        # Additional fields for the employee model (if you have one)
        user.employee.contact_number = contact
        user.employee.address = address
        user.employee.save()

        messages.success(request, 'Registration successful. You can now log in.')
        return redirect('login')  # Redirect to the login page after successful registration

    # If the request is a GET request or the form submission fails, render the registration form
    return render(request, 'auth/register.html')

def admin_view(request):
    return render(request, 'admin.html', {
        # PASS DATA
    })
    
def salary_config(request):
    return render(request, "salary-config.html", {
        
    })

def payment_proc(request):
    return render(request, "payment-proc", {
        # Return Data
    })
    
def reporting(request):
    return render(request, "reporting.html", {
        
    })
    
def system_config(request):
    return render(request, "tax-rate.html", {
        
    })
    

# <----------------------- EMPLOYEE VIEWS HERE ------------------------->
# -------------------------------------------------------------------------
# -------------------------- DASHBOARD VIEWS ------------------------------
def emp_view(request, employee_id, username, password):
    employee = Employee.get_employee_by_username_password(username, password)
    
    if employee:
        salary_info = SalaryInfo.get_salary_info_by_employee_id(employee_id)
        
        if salary_info:
            # Do something with the retrieved salary_info
            return render(request, 'user.html', {'salary_info': salary_info})
        else:
            # Handle the case when no salary info is found for the given employee_id
            return render(request, 'no_salary_info.html', {'employee_id': employee_id})
    else:
        # Handle the case when no employee is found for the given credentials
        return render(request, 'no_employee.html')

    
def pay_stub(request):
    return render(request, "user-stub.html", {
        
    })

def doc_repo(request):
    return render(request, "doc-repo.html", {
        
    })
    
# -------------------------- PROFILE MANAGEMENT VIEWS ------------------------------

def update_info(request):
    return render(request, "profile-management.html", {
        
    })
    
def change_pass(request):
    return render(request, "change-pass.html", {
        
    })
    
# -------------------------- PAYROLL VIEWS ------------------------------

def view_calculation(request):
    return render(request, "payroll.html", {
        
    })
    
def tax_info(request):
    return render(request, "tax-info.html", {
        
    })
    
# -------------------------- REPORT VIEWS ------------------------------

def user_report(request):
    return render(request, "report.html", {
        
    })
    
def tax_report(request):
    return render(request, "tax-report.html", {
        
    })
    
def financial_sum(request):
    return render(request, "financial-sum.html", {
        
    })


    
    