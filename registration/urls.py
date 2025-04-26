from django.urls import path, include
from .views import SignUp, home

urlpatterns = [
    path("signup/", SignUp.as_view(), name="signup"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", home, name="home"),
]
