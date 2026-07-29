from django.contrib import messages
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from products.models import Product
from .forms import ContactDeveloperForm

# Create your views here.

def index(request):
    """ A view to return the index page with featured popular meads"""

    popular_list = list(Product.objects.filter(most_popular=True))
    n=4
    popular_chunks = [popular_list[i:i + n] for i in range(0, len(popular_list), n)]

    context = {
        'popular_chunks': popular_chunks,
    }

    return render(request, 'home/index.html', context)


def contact_developer(request):
    if request.method == 'POST':
        contact_form = ContactDeveloperForm(data=request.POST)
        user_email = request.user.email
        user_message = request.POST.get('message')

        if contact_form.is_valid():
            email = EmailMessage(
                subject=f"New enquiry from {request.user.username}",
                body=user_message,
                from_email=None,
                to=['odrerirmeadery@gmail.com'],
                reply_to=[user_email]
            )

            email.send()

            messages.add_message(request, messages.SUCCESS, "Thank you for your message. This has been successfully sent to Óðrerir Meadery")
        else:
            messages.add_message(request, messages.ERROR, "Thank you for your message but it seems there was a problem sending this. Please try again")

    return redirect(request.META.get('HTTP_REFERER', 'home'))