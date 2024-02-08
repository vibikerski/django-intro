from django.shortcuts import render
from myapp.models import Product


def product_list(request):
    products = Product.objects.all()
    context = {
        "products_list": products
    }
    return render(
        request, 
        'myapp/product_list.html',
        context
    )

