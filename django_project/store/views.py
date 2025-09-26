from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse

from store.models import Category, Product
from store.forms import ProductForm

# def index(request):
#     return HttpResponse("<h1>Hello, world. This is home page</h1>")
#
# def about(request):
#     return HttpResponse("<h1>Hello, world. This is about page</h1>")

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def products_json(request):
    all_product = Product.objects.all()
    return JsonResponse({'products': list(all_product.values())})

def products(request):
    all_product = Product.objects.all().select_related('category').order_by('-created_at')
    return render(request, 'products.html', {'products': all_product})

def add_product(request):

    if request.method == 'POST':
        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('store:products')
    else:
        form = ProductForm()

    return render(request, 'add_product.html', {'form': form})

def update_product(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)

        if form.is_valid():
            form.save()
            return redirect('store:product_detail', product_pk=product_pk)
    else:
        form = ProductForm(instance=product)

    return render(request, 'update_product.html', {'form': form})

def delete_product(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk)

    if request.method == 'POST':
        product.delete()
        return redirect('store:products')
    return redirect('store:product_detail', product_pk=product_pk)

def product_detail(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk)
    return render(request, 'product_detail.html', {'product': product})










