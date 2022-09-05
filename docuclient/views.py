from django.shortcuts import render, redirect

# Create your views here.

from django.views.generic.detail import DetailView

from django.views.generic.list import ListView

# mes importations


from django.shortcuts import get_object_or_404

from django.urls import reverse


from .models import ( Ravite, BonLivraison, Facture, DevisClient)

from alldetail.models import Articles, Product

from django_xhtml2pdf.utils import generate_pdf



from django.contrib import messages

from django.views.decorators.csrf import csrf_protect

from django.contrib.auth.decorators import login_required

from django.views.generic import DetailView, CreateView, DeleteView, View

from django.views.generic.edit import UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# importing the necessary libraries
from django.http import HttpResponse

from .process import html_to_pdf 

from django.template.loader import render_to_string

from carts.models import Order

from carts.views import order_details

from django.views.generic.list import MultipleObjectMixin





###########################################################################################################

                     #   /***************CREATION  ******************/

##########################################################################################################

class RaviteCreateView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = Ravite
    fields = ['shop_name','article_name','article_number','article_description']

    def test_func(self):
        if self.request.user.is_superuser or self.request.user.is_staff:
            return True
        return False



class DevisClientCreateView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = DevisClient
    fields = ['payment_modality','nation_choices','client_type','client_Name','address','postal_Code',
    'phone_number','email_Address','taxe_TPS','taxe_CSS','livraison']

    def test_func(self):
        if self.request.user.is_superuser or self.request.user.is_staff:
            return True
        return False



class FactureCreateView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = Facture
    fields = ['partenary_code','reduction_number','payment_modality','modalite_paiement','nation_choices',
    'livraison']

    def test_func(self):
        if self.request.user.is_superuser or self.request.user.is_staff:
            return True
        return False



class BonLivraisonCreateView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = BonLivraison
    fields = ['client_name','client_service','client_address','client_email','phone_number']

    def test_func(self):
        if self.request.user.is_superuser or self.request.user.is_staff:
            return True
        return False



###########################################################################################################

                     #   /***************FIN DES CREATIONS  ******************/

##########################################################################################################


def alldocuments(request):

    return render(request,'docuclient/alldocument.html')


###########################################################################################################

                     #   /***************BonLivraison ******************/

##########################################################################################################


def BonLivraisonList(request):

    bonlivraisons = BonLivraison.objects.all().order_by('-date_created')

    bonlivraisons = list(bonlivraisons)

    bonlivraisons_total_number = BonLivraison.objects.all().count()

    context = {"bonlivraisons": bonlivraisons, 
    "bonlivraisons_total_number":bonlivraisons_total_number}

    return render(request, "docuclient/livraison_list.html", context)

class BonLivraisonDetail(DetailView):

    templates_name = "docuclient/bonlivraison_detail.html"

    model = BonLivraison






###########################################################################################################

                     #   /***************Facture ******************/

##########################################################################################################


def FactureClientList(request):

    factures = Facture.objects.all().order_by('-date_created')

    factures = list(factures)

    total_number = Facture.objects.all().count()

    context = {"factures": factures, "total_number":total_number}

    return render(request, "docuclient/facture_list.html", context)


class FactureCLIENTDetail(DetailView):

    templates_name = "docuclient/facture_detail.html"
    
    model = Facture

    def get_context_data(self, ** kwargs):

        context = super(FactureCLIENTDetail, self).get_context_data( ** kwargs)
        #context['name', 'barcode', 'description','price','quantite_client','article_id','product','model'] = Articles.objects.all()
        context['items','is_ordered','owner','ref_code','date_ordered'] = Order.objects.all()
        
        return context




    



###########################################################################################################

                     #   /***************Ravitaillement ******************/

##########################################################################################################


def DevisClientList(request):

    devisClients = DevisClient.objects.all().order_by('-created')

    devisClients = list(devisClients)

    total_number = DevisClient.objects.all().count

    context = {"devisClients": devisClients, 
    'total_number':total_number}

    return render(request, "docuclient/devisClients_list.html", context)

class DevisClientDetail(DetailView):

    templates_name = "docuclient/devisClients_detail.html"

    model = DevisClient

###########################################################################################################

                     #   /***************Ravitaillement ******************/

##########################################################################################################


def RaviteList(request):

    ravites = Ravite.objects.all().order_by('-date_created')

    ravites = list(ravites)

    total_number = Ravite.objects.all().count()

    context = {"ravites": ravites, 
    "total_number":total_number}

    return render(request, "docuclient/ravites_list.html", context)

class RaviteDetail(DetailView):

    templates_name = "docuclient/ravite_detail.html"

    model = Ravite
