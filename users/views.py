from django.shortcuts import render, redirect

# Create your views here.

from django.views.generic.detail import DetailView

from django.contrib import messages

from .forms import (UserRegisterForm, UserUpdateForm, LoginForm, ProfileUpdateForm, DemandeAccessForm)

from django.views.decorators.csrf import csrf_protect

from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import User, auth


# Create your views here.

#profile ####################################################
@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance = request.user)

        p_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)

        if u_form.is_valid() or p_form.is_valid():
            u_form.save()
            p_form.save()

            username = u_form.cleaned_data.get('username')

            messages.success(request,'{} votre compte a bien été modifié et merci d\'avoir choisi christ-dev'.format(username))
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance = request.user)
        
        p_form = ProfileUpdateForm(instance = request.user.profile)

    return render(request,'users/users_profile.html', {'u_form':u_form,'p_form':p_form})

#fin du profile############################################################


# partie registraction#############################################

@csrf_protect
def register(request):
    if request.method == "POST":

        form = UserRegisterForm(request.POST)

        if form.is_valid():

            form.save()

            username = form.cleaned_data.get('username')

            messages.success(request,'{} LAPTOP GABON vous remercie d\'avoir crée votre compte.'.format(username))

            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html', {'form_register':form})

############################fin de la partie registration########################

################################ page de connexion #####################
@csrf_protect
def login(request):
    form = LoginForm(request.POST or None)
    context = {'form':form}
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request,'les informations entrées sont invalid')
            return redirect('login')
    else:
        return render(request,'users/connexion.html',context)

###################################### fin du login ########################################
@login_required()
def users(request):
    users = User.objects.all()
    users = list(users)

    total_number = User.objects.all().count

    context = {'users':users,'total_number':total_number}

    return render(request,'users/users_list.html', context)

class UsersDetail(DetailView):

    templates_name = "auth/user_detail.html"

    model = User
@login_required()
def logout(request):
    auth.logout(request)
    return render(request,'users/deconnexion.html')