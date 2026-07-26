from django.shortcuts import render
from products.models import Product

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