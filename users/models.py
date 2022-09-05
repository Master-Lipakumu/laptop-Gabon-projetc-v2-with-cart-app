from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from alldetail.models import (Shop, Category, Product, Articles, ALLClientData)

from docuclient.models import ( Ravite, BonLivraison, Facture, DevisClient)

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to = "profile_pics/", default="default.jpg", blank=True)
    articles = models.ManyToManyField(Articles)
    shops= models.ManyToManyField(Shop, blank=True)
    categorys = models.ManyToManyField(Category,blank=True)
    products = models.ManyToManyField(Product,blank=True)
    ALLClientData = models.ManyToManyField(ALLClientData,blank=True)
    ravites = models.ManyToManyField(Ravite,blank=True)
    bonLivraisons = models.ManyToManyField(BonLivraison,blank=True)
    factures = models.ManyToManyField(Facture,blank=True)
    devisClients = models.ManyToManyField(DevisClient,blank=True)
    is_staff = models.BooleanField(default = False)
    last_connect = models.DateTimeField(auto_now=True)