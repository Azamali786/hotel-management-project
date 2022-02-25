from django.shortcuts import render
from django.views import View

# Create your views here.

class EmployeePortalView(View):
    """
    """
    template_name = "employees/employees_portal_page.html"

    def get(self, request):
        context = {

        }
        return render(request, self.template_name, context)