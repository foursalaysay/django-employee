from django.urls import path
from . import views

urlpatterns = [
    path("login", views.user_login, name="user_login"),
    
    # USER URLS
    path("", views.home, name="home"),
    path("register", views.register, name="register"),
    
    path("emp_view", views.emp_view, name="emp_view"),
    path("user-stub", views.user_stub, name="user_stub"),
    # path("doc-repo", views.doc_repo, name="doc_repo"),

    path("update_info", views.update_info, name="update_info"),
    path("change-pass", views.change_pass, name="change_pass"),
    
    path("view_calculation", views.view_calculation, name="view_calculation"),
    path("tax-info", views.tax_info, name="tax_info"),
    
    path("user-report", views.user_report, name="user_report"),
    path("tax-report", views.tax_report, name="tax_report"),
    path("financial-sum", views.financial_sum, name="financial_sum"),
    
    
    # ADMIN URLS
    path("admin-dashboard", views.admin_view, name="admin_view"),
    path('salary-config', views.salary_config, name="salary_config"),
    path("payment-proc", views.payment_proc, name="payment_proc"),
    path("reporting", views.reporting, name="reporting"),
    path("system-config", views.system_config, name="system_config"),
    
    path('logout/', views.logout_view, name='logout'),
    
    # ADDITIONAL
    path('search-employee/', views.search_employee, name='search_employee'),
    path('404', views.return_404, name='return_404' ),
    
    path('payment-page/<str:username>', views.payment_page, name='payment_page'),
    path('delete-employee/<str:username>/', views.delete_employee, name='delete_employee'),
    
]
