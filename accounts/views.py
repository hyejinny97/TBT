from django.shortcuts import render, redirect
from .forms import CustomCreationUserForm, CustomChangeUserForm
from .forms import CustomAuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model

# Create your views here.


def index(request):
    return render(request, "accounts/index.html")


def signup(request):
    if request.method == "POST":
        form = CustomCreationUserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect("accounts:login")
    else:
        form = CustomCreationUserForm()
    context = {"form": form}
    return render(request, "accounts/signup.html", context)


def login(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get("next") or "products:index")
    else:
        form = CustomAuthenticationForm()
    context = {"form": form}
    return render(request, "accounts/login.html", context)


def logout(request):
    auth_logout(request)
    return redirect("products:index")


def detail(request, user_pk):
    user = get_user_model().objects.get(pk=user_pk)
    context = {
        "user": user,
        "my": request.user,
    }
    return render(request, "accounts/detail.html", context)
