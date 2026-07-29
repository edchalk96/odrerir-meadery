from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def basket_contents(request):

    basket_items = []
    total = 0
    product_count = 0
    basket = request.session.get('basket', {})

    for item_id, item_data in basket.items():

        product = get_object_or_404(Product, pk=item_id)

        if isinstance(item_data, int):
            item_total = item_data * product.price
            total += item_total
            product_count += item_data
            basket_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
                'price': product.price,
            })

        elif isinstance(item_data, dict) and "items_by_volume" in item_data:
            for volume, quantity in item_data["items_by_volume"].items():
                if volume == "1L" and product.price_1l:
                    price = product.price_1l
                elif volume == "4L" and product.price_4l:
                    price = product.price_4l
                else:
                    price = product.price

                item_total = quantity * price
                total += item_total
                product_count += quantity
                basket_items.append(
                    {
                        "item_id": item_id,
                        "quantity": quantity,
                        "product": product,
                        "volume": volume,
                        "price": price,
                    }
                )

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'basket_items': basket_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context