from django.db import models
from products.models import Product

# Create your models here.
class Question(models.Model):
    MY_CHOICES = (
        ("상품", "상품"),
        ("배송", "배송"),
        ("반품", "반품"),
        ("교환", "교환"),
        ("환불", "환불"),
        ("기타", "기타"),
    )
    category = models.CharField(max_length=100, choices=MY_CHOICES)
    name = models.ForeignKey(Product, on_delete=models.CASCADE)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    check = models.BooleanField(default=False)


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
