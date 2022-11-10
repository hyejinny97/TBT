from django.shortcuts import render, redirect
from products.models import Product
from .models import Review
from .forms import ReviewForm

# Create your views here.
def main(request):
    return render(request, "reviews/main.html")


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


def delete(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    review.delete()
    return redirect("reviews:index", review.product.pk)


def update(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    if request.method == "POST":
        review_form = ReviewForm(request.POST, request.FILES, instance=review)
        if review_form.is_valid():
            review_form.save()
            return redirect("reviews:index", review.product.pk)
    else:
        review_form = ReviewForm(instance=review)
    context = {"review_form": review_form}
    return render(request, "reviews/update.html", context)
