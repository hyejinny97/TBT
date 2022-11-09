from django import forms
from .models import Product


class ProductsFrom(forms.Modelform):
    class Meta:
        model = Product
        fields = ["name", "category", "pay", "Description", "product_image", "delivery"]
        labels = {
            "name": "상푸명",
            "category": "상품분류",
            "pay": "상품가격",
            "Description": "상품설명",
            "product_image": "상품이미지",
            "delivery": "배송비",
        }
