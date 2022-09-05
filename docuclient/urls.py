
from django.urls import path, include

from .views import (alldocuments, BonLivraisonList, BonLivraisonDetail, FactureClientList, 
FactureCLIENTDetail, RaviteList, RaviteDetail, DevisClientList, DevisClientDetail, RaviteCreateView,
DevisClientCreateView, FactureCreateView, BonLivraisonCreateView)

urlpatterns = [
    # boall document
    path('', alldocuments, name="alldocuments"),
    
    # bonlivraison
    path('livraison/', BonLivraisonList, name="livraison"),
    path('livraison/<int:pk>/', BonLivraisonDetail.as_view(), name="livraison-detail"),
    path('livraison_form', BonLivraisonCreateView.as_view(), name="livraison-created"),
    
    # facture
    path('facture/', FactureClientList, name="facture"),
    path('facture/<int:pk>/', FactureCLIENTDetail.as_view(), name="facture-Detail"),
    path('facture_form', FactureCreateView.as_view(), name="facture-created"),
    
    # revitaillement
    path('ravite/', RaviteList, name="ravite"),
    path('ravite/<int:pk>/', RaviteDetail.as_view(), name="ravite-detail"),
    path('ravite_form', RaviteCreateView.as_view(), name="ravite-created"),
    # devis
    path('devisclient/', DevisClientList, name="devisclient"),
    path('devisclient/<int:pk>/', DevisClientDetail.as_view(), name="devisclient-detail"),
    path('devisclient_form', DevisClientCreateView.as_view(), name="devisclient-created"),
    
]
