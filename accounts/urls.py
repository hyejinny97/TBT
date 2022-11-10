from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = "accounts"

urlpatterns = [
    path("", views.index, name="index"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("detail/<int:user_pk>/", views.detail, name="detail"),
    # path("update/", views.update, name="update"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
