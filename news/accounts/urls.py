from django.urls import path
from .views import SignUpView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name = "signup") #SignUpView is a built in view provided by django
]
