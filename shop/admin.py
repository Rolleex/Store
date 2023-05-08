from django.contrib import admin
from .models import ProductItem, Category


# Register your models her

class ProductItemAdmin(admin.ModelAdmin):
    model = ProductItem


class CategoryAdmin(admin.ModelAdmin):
    model = Category


admin.site.register(ProductItem, ProductItemAdmin)
admin.site.register(Category, CategoryAdmin)
