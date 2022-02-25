from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),

    # url to the homepage of this project
    path("",TemplateView.as_view(template_name="bookings/home_page.html")),

    path("accounts/", include("accounts.urls", namespace="accounts")),
    path("customers/", include("customers.urls", namespace="customers")),
    path("employees/", include("employees.urls", namespace="employees")),
    path("bookings/", include("bookings.urls", namespace="bookings")),
    path("payments/", include("payments.urls", namespace="payments")),
]
