from django.db import models


class Product(models.Model):
    name = models.CharField('Name', max_length=100)
    price = models.DecimalField('Price', max_digits=8, decimal_places=2)
    stock = models.IntegerField('Amount in stock')

    def __str__(self):
        return self.name

class Client(models.Model):
    name = models.CharField('Name', max_length=100)
    last_name = models.CharField('Last name', max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.name
