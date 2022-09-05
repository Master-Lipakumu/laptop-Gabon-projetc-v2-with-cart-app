from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.contrib.auth.models import User

from datetime import datetime

from alldetail.models import Articles, ALLClientData

from users.models import Profile



class OrderItem(models.Model):
    articles = models.OneToOneField(Articles, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)
    date_ordered = models.DateTimeField(null=True)

    def __str__(self):
        return self.articles.name


class Order(models.Model):
    ref_code = models.CharField(max_length=15, null=True)
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(default=False)
    items = models.ManyToManyField(OrderItem)
    date_ordered = models.DateTimeField(auto_now=True)
    cart_facturation = models.ForeignKey('docuclient.Facture',on_delete = models.SET_NULL, null = True, related_name = "cart_facturation")

    def get_cart_items(self):
        return self.items.all()

    def get_cart_total(self):
        return sum([item.articles.price for item in self.items.all()])

    def get_cart_total_qt(self):
        return sum([item.articles.quantite_client for item in self.items.all()])

    def get_cart_total_taxes_TPS(self):
        return sum([item.articles.quantite_client for item in self.items.all()]) * sum([item.articles.price for item in self.items.all()]) - ALLClientData.taxe_TPS / 100.0

    def get_card_very_total(self):
        return sum([item.articles.price for item in self.items.all()]) * sum([item.articles.quantite_client for item in self.items.all()])

    def __str__(self):
        return '{0} - {1}'.format(self.owner, self.ref_code)


class Transaction(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    token = models.CharField(max_length=120)
    order_id = models.CharField(max_length=120)
    amount = models.DecimalField(max_digits=100, decimal_places=2)
    success = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.order_id

    class Meta:
        ordering = ['-timestamp']


class Screenshot(models.Model):
    screenshot = models.ImageField(upload_to='img/screenshots/', help_text='Html2canvas screenshot')
