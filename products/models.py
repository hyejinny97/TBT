from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=80)
    category = models.CharField(max_length=80)
    pay = models.CharField(max_length=80)
    Description = models.TextField()
    product_image = models.ImageField(null=True)
    delivery = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
