from django.urls import path
from . import views

urlpatterns = [
    path("", views.emp_view, name="home"),
    path("user/home", views.emp_view, name="emp_view"),
    path("user/user-stub", views.pay_stub, name="pay_stub"),
    path("user/doc-repo", views.doc_repo, name="doc_repo"),
    
    
    
    path("user/profile-management", views.update_info, name="update_info"),
    path("user/change-pass", views.change_pass, name="change_pass"),
    
    
    path("user/payroll", views.view_calculation, name="payroll"),
    path("user/tax-info", views.tax_info, name="tax_info"),
    
    
    path("user/user-report", views.user_report, name="user_report"),
    path("user/tax-report", views.user_tax_report, name="user_tax_report"),
    path("user/financial-sum", views.financial_sum, name="financial_sum"),
    
    
    
]
