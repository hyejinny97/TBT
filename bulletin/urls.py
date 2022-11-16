from django.urls import path
from . import views

app_name = "bulletin"

urlpatterns = [
    path("create/product_pk/", views.create, name="createQ"),
    path("delete/question_pk/", views.delete, name="deleteQ"),
    path("createA/question_pk/", views.createA, name="createA"),
    path("deleteA/answer_pk", views.deleteA, name="deleteA"),
    path("update/question_pk/", views.update, name="update"),
    path("updateA/answer_pk/", views.updateA, name="updateA"),
]
