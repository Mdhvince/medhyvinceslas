from pathlib import Path
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

from .forms import RegsiterForm, LoginForm
from .decorators import unauthenticated_only

app_name = Path("account")
# Create your views here.
def index(request):
    pass

@unauthenticated_only
def register(request):
    form = RegsiterForm()

    if request.method == "POST":
        form = RegsiterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('account:login'))
    
    context = {"form": form}
    return render(request, app_name / "register.html", context)


@unauthenticated_only
def login_view(request):
    context = {"form": LoginForm()}

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("blog:index"))
        else:
            context["message"] = "Invalid credentials."
            return render(request, app_name / "login.html", context)

    return render(request, app_name / "login.html", context)

def logout_view(request):
    logout(request)
    context = {"message": "You've been logged out."}
    return HttpResponseRedirect(reverse("account:login"), context)