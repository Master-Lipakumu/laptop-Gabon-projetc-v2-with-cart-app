from django import forms
from alldetail.models import Articles



PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 26)]

class CartAddProductForm(forms.ModelForm):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
    class Meta:
        model = Articles
        fields = ['id', 'quantity','update']
    
    