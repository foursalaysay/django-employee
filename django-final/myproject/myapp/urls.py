from django.urls import path
from . import views

urlpatterns = [
    path("", views.login, name="login"),
    
    # USER URLS
    
    path("register", views.register, name="register"),
    
    path("emp_view/", views.emp_view, name="emp_view"),
    path("pay-stub", views.pay_stub, name="pay_stub"),
    path("doc-repo", views.doc_repo, name="doc_repo"),

    path("update_info", views.update_info, name="update_info"),
    path("change-pass", views.change_pass, name="change_pass"),
    
    path("view_calculation", views.view_calculation, name="payroll"),
    path("tax-info", views.tax_info, name="tax_info"),
    
    path("user-report", views.user_report, name="user_report"),
    path("tax-report", views.tax_report, name="tax_report"),
    path("financial-sum", views.financial_sum, name="financial_sum"),
    
    
    # ADMIN URLS
    path("admin/dashboard", views.admin_view, name="admin_view"),
    path("admin/salary-config", views.salary_config, name="salary_config"),
    path("admin/payment-proc", views.payment_proc, name="payment_proc"),
    path("admin/reporting", views.reporting, name="reporting"),
    path("admin/system-config", views.system_config, name="system_config")
]
