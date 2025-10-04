from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy

from store.models import Category, Product
from store.forms import ProductForm

# def index(request):
#     return HttpResponse("<h1>Hello, world. This is home page</h1>")
#
# def about(request):
#     return HttpResponse("<h1>Hello, world. This is about page</h1>")

# def index(request):
#     return render(request, 'index.html')

class IndexView(TemplateView):
    template_name = 'index.html'

# def about(request):
#     return render(request, 'about.html')

def products_json(request):
    all_product = Product.objects.all()
    return JsonResponse({'products': list(all_product.values())})

# def products(request):
#     all_product = Product.objects.all().select_related('category').order_by('-created_at')
#     return render(request, 'products.html', {'products': all_product})

class ProductListView(ListView):
    model = Product
    template_name = 'products.html'
    context_object_name = 'products'
    queryset = Product.objects.all().select_related('category')
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = self.queryset.count()
        context['saxeli'] = 'vaniko'
        return context

# def add_product(request):
#
#     if request.method == 'POST':
#         form = ProductForm(request.POST)
#
#         if form.is_valid():
#             form.save()
#             return redirect('store:products')
#     else:
#         form = ProductForm()
#
#     return render(request, 'add_product.html', {'form': form})

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'add_product.html'
    success_url = '/products/'
    login_url = 'user:login'

# def update_product(request, product_pk):
#     product = get_object_or_404(Product, pk=product_pk)
#
#     if request.method == 'POST':
#         form = ProductForm(request.POST, instance=product)
#
#         if form.is_valid():
#             form.save()
#             return redirect('store:product_detail', product_pk=product_pk)
#     else:
#         form = ProductForm(instance=product)
#
#     return render(request, 'update_product.html', {'form': form})

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'update_product.html'
    pk_url_kwarg = 'product_pk'

    def get_success_url(self):
        return reverse_lazy('store:product_detail', kwargs={'product_pk': self.object.pk})

# def delete_product(request, product_pk):
#     product = get_object_or_404(Product, pk=product_pk)
#
#     if request.method == 'POST':
#         product.delete()
#         return redirect('store:products')
#     return redirect('store:product_detail', product_pk=product_pk)

class ProductDeleteView(DeleteView):
    model = Product
    pk_url_kwarg = 'product_pk'
    success_url = '/products/'

# def product_detail(request, product_pk):
#     product = get_object_or_404(Product, pk=product_pk)
#     return render(request, 'product_detail.html', {'product': product})

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    pk_url_kwarg = 'product_pk'
    context_object_name = 'product'








