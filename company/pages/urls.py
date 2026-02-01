from django.urls import path
from .views import home_page_view, AboutPageView

urlpatterns = [
    path("", home_page_view, name="home"),
    path("about/", AboutPageView.as_view(), name="about") #as.view is added because AboutPageView is class based view
                                            # as.view makes the class based view callable, it is mandatory to add it when using class based views
]
