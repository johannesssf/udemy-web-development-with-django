from django.shortcuts import render
from django.contrib import messages

from .forms import ContactForm, ProductModelForm
from .models import Product


def index(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'index.html', context)


def contact(request):
    form = ContactForm(request.POST or None)

    print(type(request.method))

    if request.method == 'POST':
        if form.is_valid():
            form.send_mail()

            messages.success(request, "E-mail enviado com sucesso!")
            form = ContactForm()
        else:
            messages.error(request, "Erro ao enviar e-mail!")

    context = {
        'form': form
    }
    return render(request, 'contact.html', context)


def product(request):
    if request.method == 'POST':
        form = ProductModelForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, 'Produto salvo com sucesso!')
            form = ProductModelForm()
        else:
            messages.error(request, 'Erro ao salvar produto!')
    else:
        form = ProductModelForm()

    context = {
        'form': form
    }
    return render(request, 'product.html', context)
