from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product
from .models import Review
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
import json
from django.views.decorators.http import require_POST

# Create your views here.
def index(request, product_pk):
    product = Product.objects.get(pk=product_pk)
    reviews = product.review_set.all()
    grade = 0
    cnt = 0
    for review in reviews:
        grade += review.grade
        cnt += 1
    if grade:
        grade /= cnt
    context = {
        "reviews": reviews,
        "product": product,
        "grade": grade,
    }
    return render(request, "reviews/index.html", context)


@login_required
def create(request, product_pk):
    product = Product.objects.get(pk=product_pk)
    if request.method == "POST":
        review_form = ReviewForm(request.POST, request.FILES)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.product = product
            review.account = request.user
            review.save()
            return redirect("reviews:index", product_pk)
    else:
        review_form = ReviewForm()
    context = {
        "review_form": review_form,
    }
    return render(request, "reviews/create.html", context)


@login_required
def delete(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    if request.user.pk == review.account.pk:
        review.delete()
    return redirect("reviews:index", review.product.pk)


@login_required
def update(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    if request.user.pk == review.account.pk:
        if request.method == "POST":
            review_form = ReviewForm(request.POST, request.FILES, instance=review)
            if review_form.is_valid():
                review_form.save()
                return redirect("reviews:index", review.product.pk)
        else:
            review_form = ReviewForm(instance=review)
        context = {"review_form": review_form}
    else:
        return redirect("products:index")
    return render(request, "reviews/update.html", context)


# @login_required
# def likes(request, review_pk):
#     review = Review.objects.get(pk=review_pk)
#     print(review)
#     if request.user.is_authenticated:
#         if request.user.pk != review.account.pk:
#             if review.like.filter(pk=request.user.pk).exists():
#                 review.like.remove(request.user)
#                 is_likes = False
#             else:
#                 review.like.add(request.user)
#                 is_likes = True
#     context = {"islikes": is_likes, "likecount": review.like.all().count()}
#     return JsonResponse(context)
@require_POST
def likes(request, review_pk):
    if request.user.is_authenticated:
        review = Review.objects.get(pk=review_pk)
        if review.like_users.filter(pk=request.user.pk).exists():
            review.like_users.remove(request.user)
            is_liked = False
        else:
            review.like_users.add(request.user)
            is_liked = True
        context = {
            "is_liked": is_liked,
        }
        return JsonResponse(context)
    return redirect("accounts:login")
