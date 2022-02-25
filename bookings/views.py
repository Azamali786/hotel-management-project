from django.shortcuts import render
from django.views import View

# Create your views here.

class BookingsPortalView(View):
    """
    """
    template_name = "bookings/bookings_portal_page.html"

    def get(self, request):
        context = {

        }
        return render(request, self.template_name, context)


