from django.shortcuts import render
from products.models import Product
from .models import Order, OrderItem
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def index(request):

    pdt_to_buy = request.POST.get('pdt_to_buy').split(",")
    mount_per_pdt = request.POST.get('mount_per_pdt').split(",")
    print(pdt_to_buy, mount_per_pdt)

    order_items = []
    for i in range(len(pdt_to_buy)):
        product = Product.objects.get(pk=pdt_to_buy[i])
        user = request.user
        order_item = OrderItem.objects.create(product=product, quantity=mount_per_pdt[i], user=user)
        order_items.append(order_item)

    context = {
        'order_items': order_items,
    }

    return render(request, 'orders/ordering.html', context)

def complete(request):
    products = [Product.objects.get(pk=10), Product.objects.get(pk=20), Product.objects.get(pk=30)]
 
    context = {
        'products': products,
    }
    return render(request, 'orders/order_complete.html', context)