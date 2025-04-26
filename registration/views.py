from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib import auth

# Create your views here.

@login_required
def home(request):
    return render(request, "app_base.html", {
        "username": request.user.username
    })

class SignUp(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, "registration/signup.html", {
            "form": form
        })
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        
        return render(request, "registration/signup.html", {"form": form})  # ✅ Also returns an HttpResponse