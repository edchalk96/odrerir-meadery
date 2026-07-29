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

def adjust_basket(request, item_id):
    """ Adjust the quantity of the specified product """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    volume = request.POST.get("product_volume")
    basket = request.session.get('basket', {})
    item_id_str = str(item_id)

    if volume:
        if item_id_str in basket and 'items_by_volume' in basket[item_id_str]:
            if quantity > 0:
                basket[item_id_str]["items_by_volume"][volume] = quantity
                messages.success(request, f'Updated {product.name} ({volume}) quantity to {quantity}')
            else:
                basket[item_id_str]['items_by_volume'].pop(volume, None)
                if not basket[item_id_str]["items_by_volume"]:
                    basket.pop(item_id_str, None)
                messages.success(request, f'Removed volume {volume.upper()} {product.name} from your basket')
    else:
        if quantity > 0:
            basket[item_id_str] = quantity
            messages.success(request, f'Updated {product.name} quantity to {quantity}')
        else:
            basket.pop(item_id_str, None)
            messages.success(request, f'Removed {product.name} from your basket')

    request.session['basket'] = basket
    return redirect(reverse('basket'))


def remove_from_basket(request, item_id):
    """ Remove the item from the basket """

    product = get_object_or_404(Product, pk=item_id)
    volume = request.POST.get("product_volume")
    basket = request.session.get('basket', {})
    item_id_str = str(item_id)

    try:
        if volume:
            if item_id_str in basket and 'items_by_volume' in basket[item_id_str]:
                basket[item_id_str]['items_by_volume'].pop(volume, None)
            if not basket[item_id_str]["items_by_volume"]:
                basket.pop(item_id_str, None)
            messages.success(request, f'Removed volume {volume.upper()} {product.name} from your basket')
        else:
            basket.pop(item_id_str, None)
            messages.success(request, f'Removed {product.name} from your basket')

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)