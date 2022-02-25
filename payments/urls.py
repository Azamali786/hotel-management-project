from django.urls import path
from payments import views

app_name = "employees"

urlpatterns = [ 
    path("", views.PaymentsPortalView.as_view(), name="payments_portal_page"),
]