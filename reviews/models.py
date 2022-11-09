from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.contrib.auth import get_user_model
from products.models import Product

# Create your models here.
class Review(models.Model):
    account = models.ForeignKey(get_user_model, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    content = models.TextField()
    grade = models.IntegerField()
    review_image = ProcessedImageField(
        upload_to="review_images/",
        blank=True,
        processors=[ResizeToFill(200, 200)],
        format="JPEG",
        options={"quality": 60},
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
