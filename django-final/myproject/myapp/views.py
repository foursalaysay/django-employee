from django.db import IntegrityError
from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

from . urls import *

from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash

def user_login(request):
    if request.method == 'POST':
        # Get the username and password from the form
        username = request.POST['username']
        password = request.POST['password']

        # Query the Employee model to get the user(s)
        users = Employee.objects.filter(username=username)
        
        if username == 'admin' and password == 'admin':
            return redirect('admin_view')

        if users.exists():
            # Iterate through the users and check passwords
            for user in users:
                if user.check_password(password):
                    # Log in the first user that matches the password
                    auth_login(request, user)
                    request.session['logged_in_user'] = username
                    request.session['username'] = username
                    return redirect('emp_view')

        # Authentication failed, display an error message
        return render(request, 'auth/login.html', {'error_message': 'Invalid username or password'})

    # If it's a GET request, render the login form
    return render(request, 'auth/login.html')


from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib import messages

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
            user = Employee.objects.create_user(username=username, password=password, email=email)
            
            # Add additional fields to the user model
            user.name = name
            user.contact = contact
            user.address = address
            user.save()

            # Log in the user after successful registration
            authenticated_user = authenticate(request, username=username, password=password)
            if authenticated_user is not None:
                login(request, authenticated_user)

            messages.success(request, 'Registration successful. You are now logged in.')
            return redirect('emp_view')  # Redirect to the home page after successful registration and login

        except IntegrityError:
            # Handle the unique constraint violation (email or username already exists)
            messages.error(request, 'Email address or username is already registered')
            return redirect('register')

    # If the request is a GET request or the form submission fails, render the registration form
    return render(request, 'auth/register.html')


def admin_view(request):
    employees = Employee.objects.all()
    return render(request, 'admin-view/admin.html', {
        'employees' : employees
    })
    
from django.shortcuts import render, get_object_or_404
from .models import Employee  # Make sure to import your Employee model



def salary_config(request):
    if request.method == 'POST':
        # Retrieve data from the form
        salary = float(request.POST.get('salary'))
        username = request.POST.get('username')

        # Get the employee associated with the username
        

        # Perform direct calculations without using functions
        basic_salary = salary * 0.8  # Replace with your actual calculation logic
        sss = basic_salary * 0.045  # Replace with your actual calculation logic
        philhealth = basic_salary * 0.05  # Replace with your actual calculation logic
        pagibig = basic_salary * 0.02  # Replace with your actual calculation logic
        total_deduction = sss + philhealth + pagibig
        net_pay = basic_salary - total_deduction

        # Save data to the database
        salary_info = SalaryInfo.objects.create(
            username=username,
            basic_salary=basic_salary,
            sss=sss,
            philhealth=philhealth,
            pagibig=pagibig,
            total_deduction=total_deduction,
            tax=1000,
            netpay=net_pay,
            date_saved=timezone.now()
        )

        messages.success(request, 'Salary configuration saved successfully!')
        return render(request, 'admin-view/salary-config/salary-config.html', {
            'basic_salary': basic_salary,
            'sss': sss,
            'philhealth': philhealth,
            'pagibig': pagibig,
            'total_deduction': total_deduction,
            'net_pay': net_pay,
            'salary_info' : salary_info
        })

    return render(request, 'admin-view/salary-config/salary-config.html')


def payment_proc(request):
    employees = Employee.objects.all()
    return render(request, "admin-view/payment-proc/payment-proc.html", {
        # Return Data
        'employees' : employees
    })
    
def reporting(request):
    employees = Employee.objects.all()
    return render(request, "admin-view/reporting/reporting.html", {
         'employees' : employees
    })
    
def system_config(request):
    return render(request, "admin-view/system-config/tax-rate.html", {
        
    })
    

# <----------------------- EMPLOYEE VIEWS HERE ------------------------->
# -------------------------------------------------------------------------
# -------------------------- DASHBOARD VIEWS ------------------------------

def emp_view(request):
    # Get the username from the session
    username = request.session.get('username')
    request.session['username'] = username

    # Check if the username is present in the session
    if username:
        # Filter salaries based on the username
        salaries = SalaryInfo.objects.filter(username=username)
        return render(request, 'user/user.html', {'salaries': salaries})
    else:
        # Handle the case where the username is not in the session
        return render(request, 'user/user.html', {'error_message': 'Username not found in session'})

    
def user_stub(request):
    username = request.session.get('username')
    request.session['username'] = username
    return render(request, "user/user-stub.html", {
        
    })
    


def doc_repo(request):
    if request.method == 'POST' and 'file' in request.FILES:
        uploaded_file = request.FILES['file']

        # Get the username from the session (assuming 'username' is stored in the session)
        username = request.session.get('username')
        request.session['username'] = username

        # Create and save a new Document instance in the database
        document = Document(file=uploaded_file)
        document.save()
        
        get_doc = Document.objects.all()
        context = {
            'get_doc' : get_doc
        }

        HttpResponse(f'Successfully uploaded {uploaded_file.name}')
        return redirect('doc_repo', context)

    return render(request, 'user/doc-repo.html')
    
# -------------------------- PROFILE MANAGEMENT VIEWS ------------------------------

def update_info(request):
    username = request.session.get('username')
    request.session['username'] = username
    
    get_info = Employee.objects.get(username=username)
    
    if request.method == 'POST':
        # Retrieve user input from the form
        new_email = request.POST.get('email')
        new_contact = request.POST.get('contact')
        new_address = request.POST.get('address')

        # Get the username from the session
        username = request.session.get('username')  # Replace 'username' with the key you use in your session

        # Get the user (Employee) instance using the username
        try:
            employee = Employee.objects.get(username=username)
        except Employee.DoesNotExist:
            # Handle the case where the user is not found
            messages.error(request, 'User not found.')
            return redirect('update_info')  # Redirect to the appropriate view

        # Update the profile information
        employee.email = new_email
        employee.contact = new_contact
        employee.address = new_address
        employee.save()

        messages.success(request, 'Profile information updated successfully!')
        return redirect('update_info')  # Replace with the actual URL to view the user profile

    return render(request, 'user/profile-management.html', {
            'get_info' : get_info
        }) # Replace 'your_template_name.html' with the actual template name
    
def change_pass(request):
    username = request.session.get('username')
    request.session['username'] = username
    if request.method == 'POST':
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        # Check if the current password is correct
        if not request.user.check_password(current_password):
            messages.error(request, 'Current password is incorrect.')
            return redirect('change_pass')

        # Check if the new password and confirm password match
        if new_password != confirm_password:
            messages.error(request, 'New password and confirm password do not match.')
            return redirect('change_pass')

        # Change the password
        request.user.set_password(new_password)
        request.user.save()

        # Update the session to prevent the user from being logged out
        update_session_auth_hash(request, request.user)

        messages.success(request, 'Password changed successfully.')
        return redirect('emp_view')  # Replace with the actual URL to view the user profile

    return render(request, 'user/change-pass.html')  # Replace 'your_template_name.html' with the actual template name
    
# -------------------------- PAYROLL VIEWS ------------------------------

def view_calculation(request):
    username = request.session.get('username')
    request.session['username'] = username# Replace 'username' with the key you use in your session

    try:
        # Get the employee associated with the username
        username = Employee.objects.get(username=username)
    except Employee.DoesNotExist:
        # Handle the case where no Employee is found
        return render(request, 'user/tax-info.html')

    # Filter SalaryInfo objects based on the associated employee
    salary_info_list = SalaryInfo.objects.filter(username=username)
        
    return render(request, 'user/payroll.html', {
        'salary_info_list':salary_info_list
    })

    

def tax_info(request):
    username = request.session.get('username')
    request.session['username'] = username

    # Define context with a default value

    # Check if the username is available in the session
    if username is not None:
        # Fetch only the necessary fields from the SalaryInfo model for the specific user
        salary_data = SalaryInfo.objects.filter(username=username)
        
        # Assign the fetched data to the context
        
            
    

    return render(request, 'user/tax-info.html', {'salary_data': salary_data})
    
# -------------------------- REPORT VIEWS ------------------------------

def user_report(request):
    username = request.session.get('username')
    request.session['username'] = username# Replace 'username' with the key you use in your session

    # Get the employee associated with the username
    user = Employee.objects.get(username=username)
    employee = user.employee  # Assuming you have a OneToOneField relationship between User and Employee

    # Filter SalaryInfo objects based on the associated employee
    user_report_list = SalaryInfo.objects.filter(employee=employee)
    return render(request, "user/report.html", {
        'user_report_list ' : user_report_list 
    })
    
def tax_report(request):
    username = request.session.get('username')
    request.session['username'] = username # Replace 'username' with the key you use in your session

    # Get the employee associated with the username
    user = Employee.objects.get(username=username)
    employee = user.employee  # Assuming you have a OneToOneField relationship between User and Employee

    # Filter SalaryInfo objects based on the associated employee
    tax_report_list = SalaryInfo.objects.filter(employee=employee)
    return render(request, "user/tax-report.html", {
        'tax_report_list' : tax_report_list
    })
    
def financial_sum(request):
    username = request.session.get('username')
    request.session['username'] = username# Replace 'username' with the key you use in your session

    # Get the employee associated with the username
    user = Employee.objects.get(username=username)
    employee = user.employee  # Assuming you have a OneToOneField relationship between User and Employee

    # Filter SalaryInfo objects based on the associated employee
    financial_sum = SalaryInfo.objects.filter(employee=employee)
    return render(request, "user/financial-sum.html", {
        'financial_sum' : financial_sum
    })


# -------------------------- REUSABLES VIEWS ------------------------------
def logout_view():
    # Redirect to another page after logout
    return redirect('login')


    
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


def search_employee(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        employee = get_object_or_404(Employee, username=username)
        return render(request, 'admin-view/salary-config/salary-config.html', {'employee': employee})

    return HttpResponse("Invalid Request")


def return_404(request):
    return render(request, '404.html')

# DOCUMENT REPOSITORY
from .models import Document
from .forms import DocumentForm

def upload_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_document')
    else:
        form = DocumentForm()

    documents = Document.objects.all()
    return render(request, 'upload_document.html', {'form': form, 'documents': documents})

def download_document(request, document_id):
    document = Document.objects.get(id=document_id)
    response = HttpResponse(document.file, content_type='application/octet-stream')
    response['Content-Disposition'] = f'attachment; filename="{document.file.name}"'
    return response

# DELETE EMPLOYEE
from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee

def delete_employee(request, username):
    # Use filter instead of get to handle the case where multiple employees have the same username
    employees_to_delete = Employee.objects.filter(username=username)

    if employees_to_delete.exists():
        # Delete each employee in the queryset
        employees_to_delete.delete()
        return redirect('admin_view')  # Redirect to some page after deletion
    else:
        # Handle the case where no employees with the specified username were found
        return render(request, '404.html')
    

def user_salary_view(request):
    username = request.user.username
    user_salary_data = SalaryInfo.objects.get(user__username=username)
    
    context = {
        'user_salary_data': user_salary_data
    }

    return render(request, 'user/user.html', context)
