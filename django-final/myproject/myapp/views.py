from django.db import IntegrityError
from django.shortcuts import render
from .models import *

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

from . urls import *

def login(request):
    if request.method == 'POST':
        # Get the username and password from the form
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Log the user in
            login(request, user)

            # Redirect based on user role
            if user.is_staff:
                return redirect('admin_view')
            else:
                return redirect('emp_view')
        else:
            # Authentication failed, display an error message
            return render(request, 'auth/login.html', {'error_message': 'Invalid username or password'})

    # If it's a GET request, render the login form
    return render(request, 'auth/login.html')

def register(request):
    if request.method == 'POST':
        # If the form is submitted
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        address = request.POST.get('address')
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if the username is already taken
        if Employee.objects.filter(username=username).exists():
            messages.error(request, 'Username is already taken')
            return redirect('register')  # Assuming 'register' is the name of your registration URL pattern

        try:
            # Try to create a new user
            user = Employee.objects.create_user(username=username, password=password, email=email, name=name, contact=contact, address=address)

            # Log in the user after successful registration
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)

            messages.success(request, 'Registration successful. You are now logged in.')
            return redirect('emp_view')  # Redirect to the home page after successful registration and login

        except IntegrityError:
            # Handle the unique constraint violation (email already exists)
            messages.error(request, 'Email address is already registered')
            return redirect('register')

    # If the request is a GET request or the form submission fails, render the registration form
    return render(request, 'auth/register.html')

def admin_view(request):
    employees = Employee.objects.all()
    return render(request, 'admin-view/admin.html', {
        'employees' : employees
    })
    
def salary_config(request):
    render(request, 'admin-salary-config.html')
    if request.method == 'POST':
        # Extract employee ID and salary from the submitted form data
        employee_id = request.POST.get('employee_id')
        salary = request.POST.get('salary')

        # Retrieve the employee instance based on the provided ID
        employee_instance = get_object_or_404(Employee, employee_id=employee_id)

        # Update the employee's salary
        employee_instance.salary = salary

        # Save other input values to the employee instance
        employee_instance.basic_salary = request.POST.get('basic-salary')
        employee_instance.sss = request.POST.get('sss')
        employee_instance.philhealth = request.POST.get('philhealth')
        employee_instance.pagibig = request.POST.get('pagibig')
        employee_instance.total_deduction = request.POST.get('total-deduction')
        employee_instance.net_pay = request.POST.get('net-pay')

        # Save the changes
        employee_instance.save()

        # Now, you can redirect or render another page as needed
        return render(request, 'admin-salary-config.html', {'message': 'Salary updated successfully'})

    # Fetch information from the Employee model based on the inputted employee ID
    inputted_employee_id = request.GET.get('employee_id')
    employee_instance = get_object_or_404(Employee, employee_id=inputted_employee_id)

    return render(request, "'admin-view/salary-config.html'", {
        'employee': employee_instance,
    })
    

def payment_proc(request):
    return render(request, "payment-proc.html", {
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
def emp_view(request):
    return render(request, 'user/user.html')
    # employee = Employee.get_employee_by_username_password(username, password)
    
    # if employee:
    #     salary_info = SalaryInfo.get_salary_info_by_employee_id(employee_id)
        
    #     if salary_info:
    #         # Do something with the retrieved salary_info
    #         return render(request, 'user.html', {'salary_info': salary_info})
    #     else:
    #         # Handle the case when no salary info is found for the given employee_id
    #         return render(request, 'no_salary_info.html', {'employee_id': employee_id})
    # else:
    #     # Handle the case when no employee is found for the given credentials
    #     return render(request, 'user/user.html')

    
def user_stub(request):
    return render(request, "user/user-stub.html", {
        
    })

def doc_repo(request):
    return render(request, "user/doc-repo.html", {
        
    })
    
# -------------------------- PROFILE MANAGEMENT VIEWS ------------------------------

def update_info(request):
    return render(request, "user/profile-management.html", {
        
    })
    
def change_pass(request):
    return render(request, "user/change-pass.html", {
        
    })
    
# -------------------------- PAYROLL VIEWS ------------------------------

def view_calculation(request):
    return render(request, "user/payroll.html", {
        
    })
    
def tax_info(request):
    return render(request, "user/tax-info.html", {
        
    })
    
# -------------------------- REPORT VIEWS ------------------------------

def user_report(request):
    return render(request, "user/report.html", {
        
    })
    
def tax_report(request):
    return render(request, "user/tax-report.html", {
        
    })
    
def financial_sum(request):
    return render(request, "user/financial-sum.html", {
        
    })


    
# -------------------------- ADDITIONAL VIEWS ------------------------------

# -------------------------- CHANGE PASSWORD ------------------------------
def change_password_view(request):
    if request.method == 'POST':
        user = request.user
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        # Authenticate the user with the current password
        authenticated_user = authenticate(request, username=user.username, password=current_password)

        if authenticated_user:
            # Check if the new password and confirm password match
            if new_password == confirm_password:
                # Update the password using the set_password method
                user.set_password(new_password)
                user.save()
                
                # Log the user in with the updated password
                login(request, user)

                messages.success(request, 'Password changed successfully.')
                return redirect('change_password')
            else:
                messages.error(request, 'New password and confirm password do not match.')
        else:
            messages.error(request, 'Current password is incorrect.')

    return render(request, 'your_template.html')  # Replace 'your_template.html' with your actual template
