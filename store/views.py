from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from store.models import Product, Cart, Order

# Create your views here.

def index(request):
    products = Product.objects.all()
    context = {"products":products}
    return render(request, 'store/index.html', context=context)


def product_detail(request,slug):
     product = get_object_or_404(Product,slug=slug)
     context = {"product":product}
     return render(request, "store/detail.html", context=context)

def add_to_cart(request, slug):
    user = request.user
    product = get_object_or_404(Product, slug=slug)
    cart,_ = Cart.objects.get_or_create(user=user)
    order, created = Order.objects.get_or_create(user=user, ordered=False, product=product)

    if created:
        cart.orders.add(order)
        cart.save()
    else:
        order.quantity+=1
        order.save()
    return redirect(reverse("product", kwargs={"slug": slug}))


def cart(request):
    cart = get_object_or_404(Cart, user=request.user)
    return render(request,"store/cart.html", context={"orders":cart.orders.all()})

def delete_cart(request):
    if cart := request.user.cart:
        cart.delete()
    return redirect('index')

