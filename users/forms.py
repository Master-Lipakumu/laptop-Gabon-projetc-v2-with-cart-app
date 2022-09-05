from django.contrib.auth.models import User, auth

from django.contrib.auth.forms import UserCreationForm

from django import forms

from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    nom = forms.CharField(max_length = 80, required=True)
    prenom = forms.CharField(max_length = 80,required=True)

    class Meta():
        model = User
        fields =['username','password1','password2','nom','prenom','email']



##################login form##############################
class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)
    class Meta():
        fields =['username','password']

#mise a jour des donnée

class UserUpdateForm(forms.ModelForm):
    email=forms.EmailField()
    class Meta():
        model = User
        fields = ['email','username']


# mise a jour du profile

class ProfileUpdateForm(forms.ModelForm):
    class Meta():
        model = Profile
        fields = ['image']



class DemandeAccessForm(forms.Form):
    access = forms.CharField(max_length = 28, required=True)
    class Meta():
        fields = ['access']