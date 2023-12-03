from django.shortcuts import render
from .models import Product  # Use an uppercase 'P'

# ...

def products(request):
    products = Product.objects.all()
    return render(request, 'products/products.html', {'products': products})

def product(request):
    return render(request, 'products/product.html' )
  
