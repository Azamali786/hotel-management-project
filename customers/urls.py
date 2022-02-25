from django.urls import path
from customers import views

app_name = "bookings"

urlpatterns = [ 
    path("", views.CustomerPortalView.as_view(), name="customers_page"),
]