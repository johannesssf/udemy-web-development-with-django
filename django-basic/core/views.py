from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader

from .models import Product


def index(request):
    products = Product.objects.all()

    context = {
        'course': 'Programação Web com Django Framework',
        'other': 'Django é massa!',
        'products': products,
    }
    return render(request, 'index.html', context)


def contact(request):
    return render(request, 'contact.html')


def product(request, id):
    # prod = Product.objects.get(id=id)
    prod = get_object_or_404(Product, id=id)
    context = {
        'product': prod
    }

    return render(request, 'product.html', context)


def error404(request, exception):
    # return render(request, '404.html')
    template = loader.get_template('404.html')
    return HttpResponse(
        content=template.render(),
        content_type='text/html; charset=utf8',
        status=404,
    )


def error500(request):
    # return render(request, '500.html')
    template = loader.get_template('500.html')
    return HttpResponse(
        content=template.render(),
        content_type='text/html; charset=utf8',
        status=500,
    )
