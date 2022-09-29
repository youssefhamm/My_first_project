from django.shortcuts import render, get_object_or_404

from store.models import Product 

# Create your views here.

def index(request):
    products = Product.objects.all()
    context = {"products":products}
    return render(request, 'store/index.html', context=context)


def product_detail(request,slug):
     product = get_object_or_404(Product,slug=slug)
     context = {"product":product}
     return render(request, "store/detail.html", context=context)