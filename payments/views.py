from django.shortcuts import render
from django.views import View

# Create your views here.

class PaymentsPortalView(View):
    """
    """
    template_name = "payments/payments_portal_page.html"

    def get(self, request):
        context = {

        }
        return render(request, self.template_name, context)