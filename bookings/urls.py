from django.urls import path
from bookings import views

app_name = "bookings"

urlpatterns = [ 
    path("", views.BookingsPortalView.as_view(), name="bookings_page"),
]