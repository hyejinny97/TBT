from django.shortcuts import render
from products.models import Product

# Create your views here.
def index(request):
    products = [Product.objects.get(pk=10), Product.objects.get(pk=20), Product.objects.get(pk=30)]
 
    context = {
        'products': products,
    }
    return render(request, 'orders/ordering.html', context)