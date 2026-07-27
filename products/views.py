from django.core.paginator import Paginator
from django.db.models.functions import Lower
from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def all_products(request):
    """ A view to show all products, including sorting and filtering by category"""

    products = Product.objects.all()
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'clearance' in request.GET:
            products = products.filter(clearance=True)

        if 'most_popular' in request.GET:
            products = products.filter(most_popular=True)

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            category_code = request.GET['category']
            products = products.filter(mead_type__mead_type__iexact=category_code)
            categories = Category.objects.filter(mead_type__iexact=category_code)

    current_sorting = f'{sort}_{direction}'

    paginator = Paginator(products, 12) # Show 12 products per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'products': page_obj,
        'all_products': page_obj,
        'current_categories': categories,
        'current_sorting': current_sorting,
        "page_obj": page_obj,
        "is_paginated": page_obj.has_other_pages(),
        "sort": sort,
        "direction": direction,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):    
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)