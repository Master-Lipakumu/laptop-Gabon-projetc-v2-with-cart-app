from django.db import models, transaction

# Create your models here.

from django.contrib.auth import get_user_model

from phonenumber_field.modelfields import PhoneNumberField

import barcode

from barcode.writer import ImageWriter

from io import BytesIO

from django.core.files import File

#from docuclient.models import Facture, BonLivraison, DevisClient, Ravite

from django.urls import reverse

from django.core.validators import MaxValueValidator, MinValueValidator

from django.contrib.contenttypes.models import ContentType

from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation


# Create your models here.

User = get_user_model()



""" 

########################################################################################################


              #  /***************** BOUTIQUE DATA BASE ********************/
########################################################################################################



"""

class Shop(models.Model):

    date_created = models.DateTimeField(auto_now_add=True)

    date_updated = models.DateTimeField(auto_now=True)

    shop_image = models.ImageField(upload_to='shopimages/')

    name = models.CharField(max_length=255)

    responsable_name = models.CharField(max_length=255)

    email = models.EmailField(max_length = 254)

    phone_number = PhoneNumberField()

    description = models.TextField(blank=True)

    localisation = models.CharField(max_length = 255)

    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    active = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("shop-detail", kwargs = {"pk":self.pk})

    def __str__(self):

        return self.name

    @transaction.atomic
    def disable(self):

        if self.active is False:

            return

        self.active = False

        self.save()

        self.categorys.update(active=False)


""" 

########################################################################################################


             #   /***************** CATEGORY DATA BASE ********************/
########################################################################################################



"""




class Category(models.Model):

    date_created = models.DateTimeField(auto_now_add=True)

    date_updated = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=255)

    description = models.TextField(blank=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)

    active = models.BooleanField(default=False)

    shop = models.ForeignKey('alldetail.Shop', on_delete=models.CASCADE, related_name='categorys')

    def get_absolute_url(self):
        return reverse("category-detail", kwargs = {"pk":self.pk})

    def __str__(self):

        return self.name

    @transaction.atomic
    def disable(self):

        if self.active is False:

            return
        self.active = False

        self.save()

        self.products.update(active=False)




""" 

########################################################################################################


             #  /***************** PRODUCT DATA BASE ********************/
########################################################################################################



"""




class Product(models.Model):

    date_created = models.DateTimeField(auto_now_add=True)

    date_updated = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=255)

    description = models.TextField(blank=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    active = models.BooleanField(default=False)

    category = models.ForeignKey('alldetail.Category', on_delete=models.CASCADE, related_name='products')

    def get_absolute_url(self):
        return reverse("product-detail", kwargs = {"pk":self.pk})

    def __str__(self):

        return self.name

    @transaction.atomic
    def disable(self):

        if self.active is False:

            return

        self.active = False

        self.save()

        self.articles.update(active=False)




""" 

########################################################################################################


             #   /***************** CLIENT Particulier data BASE ********************/
########################################################################################################



"""

class ALLClientData(models.Model):

    NATION = [
        ('National', 'National'),
        ('International', 'International'),
    ]

    DOCU = [
        ('Bon de livraison', 'Bon de livraison'),
        ('Devis', 'Devis'),
        ('Facture', 'Facture'),
    ]

    TYPEPAYMENT = [
        ('A échéance','A échéance'),
        ('Définis dans le contrat','Définis dans le contrat'),
        ('Journalier, hebdomadaire, mensuel','Journalier, hebdomadaire, mensuel'),
        ('Cash','Cash'),
    ]

    type_payment = models.CharField(choices=TYPEPAYMENT, blank=True, null=True, max_length=200)

    nation_choices = models.CharField(choices=NATION, blank=True, null=True, max_length=100)

    document_choices = models.CharField(choices=DOCU, blank=True, null=True, max_length=100)

    client_Name = models.CharField(null=True, blank=True, max_length=200)

    address = models.CharField(null=True, blank=True, max_length=255)

    postal_Code = models.CharField(null=True, blank=True, max_length=10)

    phone_number = PhoneNumberField()

    email_Address = models.EmailField(null=True, blank=True, max_length=200)

    partenary_code = models.CharField(max_length = 200, blank = True, null=True)

    taxe_TPS = models.FloatField(null=True, blank=True)

    taxe_CSS = models.FloatField(null=True, blank=True)

    remise = models.FloatField(null=True, blank=True)

    livraison = models.CharField(null=True, blank=True, max_length=200)

    modalite_paiement = models.FloatField(blank=True, null=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    client_cart_facturation = models.ForeignKey('carts.Order',on_delete = models.SET_NULL, null = True, blank=True, related_name = "client_cart_facturation")

    client_cart_facturation_2 = models.ForeignKey('carts.OrderItem',on_delete = models.SET_NULL, null = True, blank=True, related_name = "client_cart_facturation_2")

    date_created = models.DateTimeField(auto_now_add = True)

    last_updated = models.DateTimeField(auto_now = True)

    wait_money = models.FloatField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse("detailallclientdata", kwargs = {"pk":self.pk})

    def __str__(self):
        return f'document type {self.document_choices}, nom: {self.client_Name}, phone {self.phone_number}'

    def get_author(self):
        return f'{self.author.username}'



""" 

########################################################################################################


               # /***************** ARTICLE DATA BASE ********************/
########################################################################################################



"""




class Articles(models.Model):

    date_created = models.DateTimeField(auto_now_add=True)

    date_updated = models.DateTimeField(auto_now=True)

    model = models.CharField(max_length = 255, blank = False)

    name = models.CharField(max_length=255, blank = False)

    article_image = models.ImageField(upload_to='Articleimages/', blank = False)

    barcode = models.ImageField(upload_to='barcodeimages/', blank=True)

    article_id = models.CharField(max_length = 12, null=True)

    description = models.TextField(blank = False)

    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False)

    active = models.BooleanField(default = False, null = True, blank = False)

    price = models.FloatField(validators=[MinValueValidator(25.0)], 
    blank = False, null = True, default = 25.0)

    quantite_client = models.FloatField(validators=[MinValueValidator(1.0)], 
    blank=True, null=True, default = 1.0)

    product = models.ForeignKey('alldetail.Product', on_delete=models.CASCADE, related_name='articles')

    likes = models.ManyToManyField(User, related_name='article_like')

    facture = models.ForeignKey('docuclient.Facture',on_delete = models.SET_NULL, null = True, related_name = "facture_article")

    favouriteFacture = models.ForeignKey('docuclient.Facture', on_delete = models.SET_NULL, null = True, related_name = "favouriteFacture")

    devisClientType = models.ForeignKey('docuclient.DevisClient', on_delete = models.SET_NULL, null = True, blank = True, related_name = "devisClientType")

    bonlivraison = models.ForeignKey('docuclient.BonLivraison', on_delete = models.SET_NULL, null = True, blank = True, related_name = "bonlivraison")

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null = True, blank = False)

    object_id = models.PositiveIntegerField(null = True, blank = False)

    content_object = GenericForeignKey()

    def get_absolute_url(self):
        return reverse("articles-detail", kwargs = {"pk":self.pk})

    def number_of_likes(self):
        return self.likes.count()

    def name_of_article(self):
        return self.name.count()

    def __str__(self):
        return f'Article by {self.author} on {self.name}'

    def save(self, *args, **kwargs):

        EAN = barcode.get_barcode_class('ean13')

        ean = EAN(f'{self.article_id}{self.name}{self.model}', writer=ImageWriter())

        buffer = BytesIO()

        ean.write(buffer)

        self.barcode.save(f'{self.article_id}.png', File(buffer), save=False)

        return super().save(*args, **kwargs)

    @property
    def facture_data(self):
        all_data = [
        self.facture.partenary_code,
        self.facture.reduction_number,
        self.facture.payment_modality,
        self.facture.modalite_paiement,
        self.facture.date_created,
        self.facture.last_updated,
        self.facture.author,
        self.facture.nation_choices,
        self.facture.livraison,
        self.facture.active]
        return all_data

    def montant_total(self):
        return self.quantite_client * self.price

    class Meta:
        indexes = [
            models.Index(fields=["content_type", "object_id"]),
        ]

