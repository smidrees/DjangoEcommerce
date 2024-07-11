from django.shortcuts import render

# Create your views here.

def store(request):
    context = {}
    return render(request, 'store/store.html', context)

def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)

def checkout(request):
    context = {}
    return render (request, 'store/checkout.html', context)

def listing(request):
    context = {}
    return render (request, "store/list.html", context)

def product_detail(request):
    context = {}
    return render (request, "store/detail.html", context)