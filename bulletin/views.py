from django.shortcuts import render, redirect
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm
from products.models import Product

# Create your views here.


def create(request, product_pk):
    product = Product.object.get(pk=product_pk)
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.product = product
            question.account = request.user
            question.save()
            return redirect("products:index")
    else:
        form = QuestionForm()
    context = {"form": form}
    return render(request, "bulletin/create.html", context)


def delete(request, question_pk):
    question = Question.objects.get(pk=question_pk)
    if request.user.pk == question.account.pk:
        question.delete()
    return redirect("products:index")


def update(
    request,
    question_pk,
):
    question = Question.objects.get(pk=question_pk)
    if request.user.pk == question.account.pk:
        if request.method == "POST":
            form = QuestionForm()(request.POST, instance=question)
            if form.is_valid():
                form.save()
                return redirect("products:index")
        else:
            form = QuestionForm(instance=question)
        context = {"form": form}
    else:
        return redirect("products:index")
    return render(request, "bulletin/update.html", context)


# Answer 쪽 crud
def createA(request, question_pk):
    question = Question.object.get(pk=question_pk)

    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.save()
            if question.answer_set.exists():
                question.check = True
            return redirect("products:index")
    else:
        form = AnswerForm()
    context = {"form": form}
    return render(request, "bulletin/createA.html", context)


def deleteA(request, answer_pk):
    answer = Answer.objects.get(pk=answer_pk)
    if request.user.pk == answer.account.pk:
        answer.delete()
    return redirect("products:index")


def updateA(
    request,
    answer_pk,
):
    answer = Answer.objects.get(pk=answer_pk)
    if request.user.pk == answer.account.pk:
        if request.method == "POST":
            form = AnswerForm()(request.POST, instance=answer)
            if form.is_valid():
                form.save()
                return redirect("products:index")
        else:
            form = AnswerForm(instance=answer)
        context = {"form": form}
    else:
        return redirect("products:index")
    return render(request, "bulletin/updateA.html", context)
