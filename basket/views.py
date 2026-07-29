from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product


def view_basket(request):
    """ A view that renders the basket contents page """

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """ Add a quantity of the specified product to the shopping basket with volume variant """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    volume = request.POST.get("product_volume")
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if volume:
        item_id_str = str(item_id)

        if item_id_str in basket:
            if isinstance(basket[item_id_str], dict):
                if volume in basket[item_id_str]["items_by_volume"]:
                    basket[item_id_str]["items_by_volume"][volume] += quantity
                    messages.success(request, f'Updated {product.name} ({volume}) quantity to {basket[item_id_str]["items_by_volume"][volume]}',)
                else:
                    basket[item_id_str]["items_by_volume"][volume] = quantity
                    messages.success(request,f"Added {product.name} ({volume}) to your basket",)
            else:
                basket[item_id_str] = {"items_by_volume": {volume: quantity}}
                messages.success(request, f"Added {product.name} ({volume}) to your basket")
        else: 
            basket[item_id_str] = {"items_by_volume": {volume: quantity}}
            messages.success(request, f"Added {product.name} ({volume}) to your basket")
    else:
        item_id_str = str(item_id)

        if item_id_str in basket:
            if isinstance(basket[item_id_str], int):
                basket[item_id_str] += quantity
            else:
                basket[item_id_str] = quantity
        else:
            basket[item_id_str] = quantity

        messages.success(request, f"Added {product.name} to your basket")

    request.session['basket'] = basket
    return redirect(redirect_url)






