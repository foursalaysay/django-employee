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
# -------------------------------------------------------------------------
# -------------------------- DASHBOARD VIEWS ------------------------------
def emp_view(request):
    return render(request, "user.html", {
        # PASS DATA
    })
    
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


    
    