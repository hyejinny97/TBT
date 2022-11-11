from django.shortcuts import render, redirect, get_object_or_404
from .form import ProductsForm, ProductImageForm
from .models import Product,ProductImage
from django.db.models import Avg, Count
# Create your views here.
def index(request):
    products = Product.objects.all()

    context = {
        'products' : products
    }
    return render(request, "products/index.html", context)


# Create your views here.
def products_create(request):
    if request.method == 'POST':
        create_form = ProductsForm(request.POST, request.FILES)
        product_images = request.FILES.getlist('image')
        if create_form.is_valid():
            product = create_form.save()
            for img in product_images:
                ProductImage.objects.create(product=product, image=img)
            return redirect('products:index')
    else:
        create_form = ProductsForm()
        product_image_form = ProductImageForm()

    context = {
        'create_form' : create_form,
        'product_image_form': product_image_form,
    }

    return render(request, 'products/products_create.html', context)

def products_index(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'products/products_index.html', context)

def products_detail(request, products_pk):
    products = get_object_or_404(Product, pk=products_pk)
    reviews = products.review_set.all()
    total = products.review_set.aggregate(review_avg=Avg('grade'))

    context = {
        'products' : products,
        'reviews' : reviews,
        'total' : total,
    }

    return render(request, 'products/products_detail.html', context)

def products_update(request, products_pk):
    products = get_object_or_404(Product, pk=products_pk)
    if request.method == "POST":
        form = ProductsForm(request.POST, request.FILES, instance=products)
        if form.is_valid():
            form.save()
            return redirect('products:products_detail', products_pk)

    else:
        form = ProductsForm(instance=products)

    context ={
        'form' : form,
    }
    
    return render(request, 'products/products_update.html', context)

def products_delete(request, products_pk):

        products = get_object_or_404(Product, pk=products_pk)
        products.delete()
        return redirect('products:index')
