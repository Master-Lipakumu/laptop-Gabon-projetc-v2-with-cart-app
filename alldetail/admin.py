from django.contrib import admin

# Register your models here.

from .models import (Category, Shop, Product, Articles, ALLClientData)



admin.site.register(Shop)

admin.site.register(Category)

admin.site.register(Product)

admin.site.register(Articles)

admin.site.register(ALLClientData)
