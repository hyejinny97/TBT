from django import forms
from .models import Product, ProductImage

class ProductsForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "category", "pay", "Description", "delivery"]
        labels = {
            "name": "상품명",
            "category": "상품분류",
            "pay": "상품가격",
            "Description": "상품설명",
            "delivery": "배송비",
        }

class ProductImageForm(forms.ModelForm):
    image = forms.ImageField(
        label='Image',
        widget=forms.ClearableFileInput(attrs={'multiple':True}),
    )
    class Meta:
        model = ProductImage
        fields = ('image', )