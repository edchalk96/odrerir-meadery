from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models.functions import Lower
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category, Review
from .forms import ReviewForm
from checkout.models import OrderLineItem


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


@login_required
def add_review(request, product_id):
    """ A view to add a review for a product """

    product = get_object_or_404(Product, pk=product_id)
    order_number = request.GET.get('order_number')

    has_purchased = OrderLineItem.objects.filter(order__user_profile__user=request.user, product=product).exists()

    if not has_purchased:
        messages.error(request, "You can only rate products you have purchased.")
        return redirect('product_detail', product_id=product.id)

    existing_review = Review.objects.filter(product=product, user=request.user).first()
    if existing_review:
        messages.error(request, "You have already rated this product.")
        if order_number:
            return redirect('order_history', order_number=order_number)
        return redirect(request.META.get('HTTP_REFERER', 'profile'))

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            messages.success(request, f"Thank you for rating {product.name}!")

            if order_number:
                return redirect('order_history', order_number=order_number)
            return redirect(request.META.get('HTTP_REFERER', 'profile'))

    return redirect(request.META.get('HTTP_REFERER', 'profile'))