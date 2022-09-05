from django.contrib import admin

# Register your models here.

from .models import (DevisClient, BonLivraison, Facture, Ravite)

admin.site.register(DevisClient)

admin.site.register(BonLivraison)

admin.site.register(Facture)

admin.site.register(Ravite)