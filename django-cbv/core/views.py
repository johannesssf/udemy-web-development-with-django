from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Product


class IndexView(ListView):
    models = Product
    template_name = 'index.html'
    queryset = Product.objects.all()
    context_object_name = 'products'


class CreateProductView(CreateView):
    model = Product
    template_name = 'product_form.html'
    fields = ['name', 'price']
    success_url = reverse_lazy('index')


class UpdateProductView(UpdateView):
    model = Product
    template_name = 'product_form.html'
    fields = ['name', 'price']
    success_url = reverse_lazy('index')


class DeleteProductView(DeleteView):
    model = Product
    template_name = 'product_del.html'
    success_url = reverse_lazy('index')
