from django.shortcuts import render

def store(request):
    context = {}
    return render(request, 'store/store.html', context)

def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)

def home(request):
    context = {}
    return render(request, 'store/home.html', context)

def contact(request):
    context = {}
    return render(request, 'store/contact.html', context)