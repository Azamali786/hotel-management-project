from django.urls import path
from employees import views

app_name = "employees"

urlpatterns = [ 
    path("", views.EmployeePortalView.as_view(), name="employees_portal_page"),
]