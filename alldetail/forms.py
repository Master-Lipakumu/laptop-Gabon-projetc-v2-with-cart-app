from django import forms

from .models import ALLClientData


class ALLClientDataFrom(forms.ModelForm):

    class Meta:
        model = ALLClientData
        fields = ('id','client_Name','address','postal_Code','phone_number','document_choices',
        'nation_choices', 'type_payment','email_Address','partenary_code','taxe_TPS','taxe_CSS',
        'remise','livraison','modalite_paiement','client_cart_facturation')