from django.urls import path
from django.views.generic import TemplateView
from accounts import views

app_name = "accounts"

urlpatterns = [

    # this is accounts_page where options for register and login is available
    path("", TemplateView.as_view(template_name="accounts/accounts_page.html"), name="accounts_page"),
    
    path("register/", views.UserRegistrationView.as_view(), name="registration_page"),
    # path("login/", views.UserRegistrationView.as_view(), name="login_page"),
    # path("logout/", views.UserRegistrationView.as_view(), name="logout_page"),
]