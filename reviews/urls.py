from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = "reviews"

urlpatterns = [
    path("<int:product_pk>/", views.index, name="index"),
    path("<int:product_pk>/create/", views.create, name="create"),
    path("delete/<int:review_pk>/", views.delete, name="delete"),
    path("update/<int:review_pk>/", views.update, name="update"),
    path("like/<int:review_pk>/", views.likes, name="likes"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
