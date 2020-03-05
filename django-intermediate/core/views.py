from django.shortcuts import render
from django.contrib import messages

from .forms import ContactForm


def index(request):
    return render(request, 'index.html')


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
    return render(request, 'product.html')
