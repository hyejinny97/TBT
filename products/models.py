from django.db import models
from imagekit.models.fields import ProcessedImageField
from imagekit.processors import ResizeToFill


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=80)
    category = models.CharField(max_length=80)
    pay = models.CharField(max_length=80)
    Description = models.TextField()
    delivery = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    sale = models.TextField()
    product_image = ProcessedImageField(
        upload_to="imgaes/",
        blank=True,
        processors=[ResizeToFill(400, 400)],  
        format="JPEG",
        options={"quality": 60},  
    )
