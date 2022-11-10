from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.


class User(AbstractUser):
    nickname = models.CharField(max_length=20)
    followings = models.ManyToManyField(
        "self", symmetrical=False, related_name="followers"
    )
    profile_image = ProcessedImageField(
        upload_to="media/",
        blank=True,
        processors=[ResizeToFill(100, 100)],
        format="JPEG",
        options={"quality": 60},
    )

    def profile_image1(self):
        if self.profile_image and hasattr(self.profile_image, "url"):
            return self.profile_image.url
        else:
            return (
                "https://kr.seaicons.com/wp-content/uploads/2015/08/green-user-icon.png"
            )
