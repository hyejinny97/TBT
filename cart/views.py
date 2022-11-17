from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product, ProductImage
from .models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def add_cart(request, product_pk):
    product = Product.objects.get(pk=product_pk)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id=_cart_id(request))
        cart.save()

    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(product=product, quantity=1, cart=cart)
        cart_item.save()
    return redirect("cart:cart_detail")


def cart_detail(
    request,
    total=0,
    counter=0,
    cart_items=None,
    totalcount=0,
    pay_total=0,
    sale=0,
):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart_id=cart.pk)
        totalcount = len(cart_items)
        for cart_item in cart_items:
            print(cart_item.product.pk)
            total = cart_item.product.pay * cart_item.quantity
            counter += cart_item.quantity
            product = Product.objects.get(pk=cart_item.product.pk)
            sale = product.sale
            print(total * (100 - sale) * 0.01)
            pay_total += total * (100 - sale) * 0.01

    except ObjectDoesNotExist:
        pass

    return render(
        request,
        "cart/cart.html",
        dict(
            cart_items=cart_items,
            total=total,
            counter=counter,
            total_count=totalcount,
            pay_total=pay_total,
            sale=sale,
        ),
    )


def cart_remove(request, product_pk):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, pk=product_pk)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect("cart:cart_detail")


def cart_delete(request, product_pk):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, pk=product_pk)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    cart_item.delete()
    return redirect("cart:cart_detail")
