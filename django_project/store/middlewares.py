from django.urls import resolve
from django.utils.deprecation import MiddlewareMixin
from store.models import Product

class ProductCountMiddleware(MiddlewareMixin):

    def process_view(self, request, view_func, view_args, view_kwargs):

        resolver = resolve(request.path_info)

        if resolver.view_name == 'store:product_detail':
            product_pk = view_kwargs.get('product_pk')

            if product_pk:
                product = Product.objects.get(pk=product_pk)
                product.views += 1
                product.save(update_fields=['views'])
        return None

    def process_request(self, request):
        print("Middleware Executed from request")

    def process_response(self, request, response):
        print("Middleware Executed from response")
        return response

