from multiprocessing import context
from django.shortcuts import redirect, render
from django.views import View
from django.contrib import messages

# Create your views here.

class UserRegistrationView(View):
    template_name = "accounts/registration.html"
    # form = UserRegistrationForm

    def get(self, request):
        context = {
            # "form": form 
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form(request.POST)
        context = {
            # "form": form 
        }
        if form.is_valid():
            # save form and do futhr operation 

            messages.success(request, "you registration is successfull, you can login now")
            return redirect("login")

        messages.success(request, "some incorrect fields are there, please correct them")
        return render(request, self.template_name, context)


