from .models import Product, Category


def global_settings(request):

    all_product = Product.objects.all()
    category = Category.objects.all()

    return {
        'site_name': 'My Store',
        'all_product': all_product,
        'category': category,
        'saxeli': 'vaniko'
    }
