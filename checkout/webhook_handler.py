from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .models import Order, OrderLineItem
from products.models import Product
from profiles.models import UserProfile

import json
import time
import stripe


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """Send the user a confirmation email"""
        cust_email = order.email
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order': order})
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        pid = intent.id

        basket = intent.metadata['basket'
                                 ] if 'basket' in intent.metadata else '{}'
        save_info = intent.metadata['save_info'
                                    ] if 'save_info' in intent.metadata else 'false'
        username = intent.metadata['username'
                                   ] if 'username' in intent.metadata else 'AnonymousUser'

        stripe_charge = stripe.Charge.retrieve(
            intent.latest_charge
        )

        billing_details = stripe_charge.billing_details
        shipping_details = intent.shipping
        grand_total = round(stripe_charge.amount / 100, 2)

        # Clean data in the shipping details
        shipping_address = shipping_details.address.to_dict() if hasattr(
            shipping_details.address, 'to_dict') else dict(
                shipping_details.address)

        for field, value in shipping_address.items():
            if value == "":
                shipping_address[field] = None

        # Update profile information if save_info was checked
        profile = None
        if username != 'AnonymousUser':
            try:
                profile = UserProfile.objects.get(user__username=username)
                if save_info == 'true' or save_info is True:
                    profile.default_country = shipping_address.get(
                        'country')
                    profile.default_postcode = shipping_address.get(
                        'postal_code')
                    profile.default_town_or_city = shipping_address.get(
                        'city')
                    profile.default_street_address1 = shipping_address.get(
                        'line1')
                    profile.default_street_address2 = shipping_address.get(
                        'line2')
                    profile.default_county = shipping_address.get(
                        'state')
                    profile.save()
            except UserProfile.DoesNotExist:
                profile = None

        order_exists = False
        attempt = 1

        email = getattr(billing_details, 'email',
                        None) or 'unknown@example.com'
        raw_phone = getattr(shipping_details,
                            'phone', None) if shipping_details else None
        phone_number = raw_phone if (raw_phone and str(
            raw_phone).strip() != "") else '0000000000'

        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=email,
                    phone_number__iexact=phone_number,
                    country__iexact=shipping_address.get('country'),
                    postcode__iexact=shipping_address.get('postal_code'),
                    town_or_city__iexact=shipping_address.get('city'),
                    street_address1__iexact=shipping_address.get('line1'),
                    street_address2__iexact=shipping_address.get('line2'),
                    county__iexact=shipping_address.get('state'),
                    grand_total=grand_total,
                    original_basket=basket,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            self._send_confirmation_email(order)
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    user_profile=profile,
                    email=email,
                    phone_number=phone_number,
                    country=shipping_address.get('country'),
                    postcode=shipping_address.get('postal_code'),
                    town_or_city=shipping_address.get('city'),
                    street_address1=shipping_address.get('line1'),
                    street_address2=shipping_address.get('line2'),
                    county=shipping_address.get('state'),
                    grand_total=grand_total,
                    original_basket=basket,
                    stripe_pid=pid,
                )
                for item_id, item_data in json.loads(basket).items():
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    else:
                        for volume, quantity in item_data['items_by_volume'
                                                          ].items():
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_volume=volume,
                            )
                            order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        self._send_confirmation_email(order)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
