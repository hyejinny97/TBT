from django.urls import path
from . import views

app_name = "bulletin"

urlpatterns = [
    path("create/product_pk/", views.create, name="create"),
]
