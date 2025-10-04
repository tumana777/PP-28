from django.contrib import admin
from store.models import Category, Product

# admin.site.register([Category, Product])

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'quantity', 'is_available', 'views']
    # list_display_links = ('price',)
    list_filter = ('is_available', 'price')
    list_editable = ('price', 'quantity')
    search_fields = ('title', 'description')
    actions = ('make_product_available', 'make_product_not_available')
    readonly_fields = ('views',)

    @admin.action(description='Make Product Available')
    def make_product_available(self, request, queryset):
        queryset.update(is_available=True)

    @admin.action(description='Make Product Not Available')
    def make_product_not_available(self, request, queryset):
        queryset.update(is_available=False)