from django.contrib import admin
from .models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'mead_type',
        'price',
        'rating',
        'image',
        'stock_level',
    )
    ordering = ('sku',)
    search_fields = ('name', 'sku')
    list_filter = ('stock_level')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'mead_type',
    )