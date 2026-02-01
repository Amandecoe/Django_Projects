from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
def home_page_view(request):
    context = {
        "inventory_list": ["Jordan", "Nike", "Addidas"],
        "greeting":"Thank You For Visiting.",
    }
    return render(request, "home.html", context)


class AboutPageView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs): #basically adds data to the template context
        context = super().get_context_data(**kwargs) #we use super() here to call the context variable defined earlier with its existing value
        context["contact_address"] = "123 Main Street" #then we add two keys
        context["phone_number"] = "555-555-555"
        return context #returns the context to the template


