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
