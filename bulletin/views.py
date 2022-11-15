from django.shortcuts import render, redirect
from .models import Question, Answer
from .forms import QuestionForm
from products.models import Product

# Create your views here.


def create(request, product_pk):
    product = Product.object.get(pk=product_pk)

    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.product = product
            question.save()
            return redirect("bulletin:index")
    else:
        form = QuestionForm()
    context = {"form": form}
    return render(request, "bulletin/index.html", context)
