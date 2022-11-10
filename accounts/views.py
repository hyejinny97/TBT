from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomCreationUserForm, CustomChangeUserForm
from .forms import CustomAuthenticationForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST

# Create your views here.


def index(request):
    users = get_user_model().objects.all()
    context = {"users": users}
    return render(request, "accounts/index.html", context)


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
    return redirect("accounts:index")


def detail(request, user_pk):
    user = get_user_model().objects.get(pk=user_pk)
    context = {
        "user": user,
        "my": request.user,
    }
    return render(request, "accounts/detail.html", context)


@login_required
def update(request):
    if request.method == "POST":
        form = CustomChangeUserForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("accounts:detail", request.user.pk)
    else:
        form = CustomChangeUserForm(instance=request.user)
    context = {"form": form}
    return render(request, "accounts/update.html", context)


def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect("accounts:signup")


def changeps(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect("accounts:update")
    else:
        form = PasswordChangeForm(request.user)
    return render(request, "accounts/change_ps.html", {"form": form})


# @require_POST
# def follow(request, user_pk):
#     if request.user.is_authenticated:
#         user = get_user_model().objects.get(pk=user_pk)
#         if user != request.user:
#             if user.followings.filter(pk=request.user.pk).exists():
#                 user.followings.remove(request.user)
#                 is_followed = False
#             else:
#                 user.followings.add(request.user)
#                 is_followed = True
#             context = {
#                 "is_followed": is_followed,
#                 "followers_count": user.followers.count(),
#                 "followings_count": user.followings.count(),
#             }

#         return JsonResponse(context)
#     return redirect("accounts:login")


@login_required
def follow(request, user_pk):
    user = get_object_or_404(get_user_model(), pk=user_pk)
    if request.user != get_user_model().objects.get(pk=user_pk):
        if request.user not in get_user_model().objects.get(pk=user_pk).follower.all():
            request.user.followings.add(get_user_model().objects.get(pk=user_pk))
            is_followed = True
        else:
            request.user.followings.remove(get_user_model().objects.get(pk=user_pk))
            is_followed = False
        context = {
            "isFollowed": is_followed,
            "followers_count": user.follower.count(),
            "followings_count": user.followings.count(),
        }

    return JsonResponse(context)
