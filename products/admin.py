from django.contrib import admin
from .models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'mead_type',
        'price',
        'average_rating',
        'image',
        'stock_level',
        'clearance',
        'most_popular'
    )
    ordering = ('sku',)
    search_fields = ('name', 'sku')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'mead_type',
    )