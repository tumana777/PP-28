from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse

from store.models import Category, Product

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
    all_product = Product.objects.all()
    return render(request, 'products.html', {'products': all_product})

def product_detail(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk)
    return render(request, 'product_detail.html', {'product': product})










