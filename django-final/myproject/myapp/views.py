from django.shortcuts import render

# Create your views here.

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
def emp_view(request):
    return render(request, "user.html", {
        # PASS DATA
    })
    
