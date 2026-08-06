from decimal import Decimal

from django.shortcuts import (render, redirect, reverse,
                              HttpResponse, get_object_or_404)
from django.contrib import messages
from products.models import Product


def get_basket_total_liters_for_product(basket, product):
    """
    Calculate the total liters of a specific product in the basket,
    accounting for volume variants.
    """
    item_id_str = str(product.id)
    total_liters = Decimal('0.0')

    if item_id_str not in basket:
        return total_liters

    basket_data = basket[item_id_str]

    if isinstance(basket_data, dict) and 'items_by_volume' in basket_data:
        for volume_code, qty in basket_data['items_by_volume'].items():
            liters_per_unit = product.get_volume_in_liters(volume_code)
            total_liters += liters_per_unit * Decimal(str(qty))
    elif isinstance(basket_data, int):
        liters_per_unit = product.get_volume_in_liters(None)
        total_liters += liters_per_unit * Decimal(str(basket_data))

    return total_liters


def view_basket(request):
    """ A view that renders the basket contents page """

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """
    Add a quantity of the specified product
    to the shopping basket with volume variant
    """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    volume = request.POST.get("product_volume")
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})
    item_id_str = str(item_id)

    liters_in_basket = get_basket_total_liters_for_product(basket, product)

    new_requested_liters = product.get_volume_in_liters(
        volume) * Decimal(str(quantity))

    if (liters_in_basket + new_requested_liters > product.stock_level):
        available_liters = max(Decimal('0.0'),
                               product.stock_level - liters_in_basket)
        messages.error(
            request,
            f'Sorry, there is not enough stock for {product.name}. '
            f'You already have {liters_in_basket}L in your basket, and only {available_liters}L remains available.'
        )
        return redirect(redirect_url)

    if volume:
        item_id_str = str(item_id)

        if item_id_str in basket:
            if isinstance(basket[item_id_str], dict):
                if volume in basket[item_id_str]["items_by_volume"]:
                    basket[item_id_str]["items_by_volume"][volume] += quantity
                    messages.success(request,
                                     f'Updated {product.name} ({volume}) quantity to {basket[item_id_str]["items_by_volume"][volume]}', )
                else:
                    basket[item_id_str]["items_by_volume"][volume] = quantity
                    messages.success(request,
                                     f"Added {product.name} ({volume}) to your basket",)
            else:
                basket[item_id_str] = {"items_by_volume": {volume: quantity}}
                messages.success(request,
                                 f"Added {product.name} ({volume}) to your basket")
        else:
            basket[item_id_str] = {"items_by_volume": {volume: quantity}}
            messages.success(request,
                             f"Added {product.name} ({volume}) to your basket")
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

    if quantity > 0:
        if volume:
            other_variants_liters = Decimal('0.0')
            if item_id_str in basket and isinstance(basket[item_id_str], dict):
                for volume_code, qty in basket[item_id_str].get('items_by_volume',
                                                                {}).items():
                    if volume_code != volume:
                        other_variants_liters += product.get_volume_in_liters(
                            volume_code) * Decimal(str(qty))

            new_variant_liters = product.get_volume_in_liters(
                volume) * Decimal(str(quantity))
            total_requested_liters = other_variants_liters + new_variant_liters
        else:
            total_requested_liters = product.get_volume_in_liters(
                None) * Decimal(str(quantity))

        if total_requested_liters > product.stock_level:
            messages.error(
                request,
                f'Cannot update {product.name}. Requested quantity exceeds available stock of {product.stock_level}L.'
            )
            return redirect(reverse('basket'))

    if volume:
        if item_id_str in basket and 'items_by_volume' in basket[item_id_str]:
            if quantity > 0:
                basket[item_id_str]["items_by_volume"][volume] = quantity
                messages.success(request,
                                 f'Updated {product.name} ({volume}) quantity to {quantity}')
            else:
                basket[item_id_str]['items_by_volume'].pop(volume, None)
                if not basket[item_id_str]["items_by_volume"]:
                    basket.pop(item_id_str, None)
                messages.success(request,
                                 f'Removed volume {volume.upper()} {product.name} from your basket')
    else:
        if quantity > 0:
            basket[item_id_str] = quantity
            messages.success(request,
                             f'Updated {product.name} quantity to {quantity}')
        else:
            basket.pop(item_id_str, None)
            messages.success(request,
                             f'Removed {product.name} from your basket')

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
            messages.success(request,
                             f'Removed volume {volume.upper()} {product.name} from your basket')
        else:
            basket.pop(item_id_str, None)
            messages.success(request,
                             f'Removed {product.name} from your basket')

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
