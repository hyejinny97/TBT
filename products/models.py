from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=80)
    category = models.CharField(max_length=80)
    pay = models.CharField(max_length=80)
    Description = models.TextField()
    delivery = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    sale = models.TextField()


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/", null=True)

#  추가 모델 서브 이미지 모델 생성
