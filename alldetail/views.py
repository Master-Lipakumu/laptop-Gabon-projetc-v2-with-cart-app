from django.shortcuts import render, redirect

# Create your views here.

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.views.generic.detail import DetailView

from django.views.generic.list import ListView


# mes importations

from django.urls import reverse


from .models import (Shop, Category, Product, Articles, ALLClientData)

from django.contrib import messages

from django.views.decorators.csrf import csrf_protect

from django.contrib.auth.decorators import login_required

from django.views.generic import DetailView, CreateView, DeleteView, ListView

from django.views.generic.edit import UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

import random

from django.db.models import Q

from cart.cart import Cart

from .forms import ALLClientDataFrom



class SearchResultsView(ListView):
    model = Articles
    template_name = 'alldetail/search_results.html'

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = Articles.objects.filter(
            Q(name__icontains=query) | Q(model__icontains=query)
        )
        return object_list

###########################################################################################################

                     #   /***************UPDATE VIEW  ******************/

##########################################################################################################

class ShopUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Shop
    fields = ['shop_image','name','description','responsable_name','active','email','phone_number','localisation']

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False


class CategoryUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Category
    fields = ['name','description','active','shop']

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False




class ProductUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Product
    fields = ['name','description','active','category']

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False


class ArticleUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Articles
    fields = ['model','name','description','article_image','active','price','stock','article_id','product']

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False

class ArticleStaffUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Articles
    fields = ['facture','devisClientType','bonlivraison','quantite_client']

    def test_func(self):
        if self.request.user.is_staff:
            return True
        return False



class ALLClientDataUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = ALLClientData
    fields = '__all__'

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False






###########################################################################################################

                     #   /***************FIN DES CREATIONS  ******************/

##########################################################################################################






###########################################################################################################

                     #   /***************CREATION  ******************/

##########################################################################################################

class ArticleCreateView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = Articles
    fields = ['model','name','description','article_image','active','price','stock','article_id','product']

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False

    def choices(self):
        list1 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,25,29,30,31,32,33,34,
        35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,56,55,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,
        73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,89,88,90,91,92,93,94,95,96,97,98,99,100]
        r1 = random.randint(0, 14)
        return {'r1':r1}




class ShopCreateView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = Shop
    fields = ['shop_image','name','description','responsable_name','active','email','phone_number','localisation']

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False




class CategoryCreateView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = Category
    fields = ['name','description','active','shop']

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False





class ProductCreateView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = Product
    fields = ['name','description','active','category']

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False


class ALLClientDataCreateView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = ALLClientData
    fields = '__all__'

    def test_func(self):
        if self.request.user.is_superuser or self.request.user.is_staff:
            return True
        return False



###########################################################################################################

                     #   /***************FIN DES CREATIONS  ******************/

##########################################################################################################
@login_required()
def allclient(request):

    return render(request,'alldetail/allclient.html')



###########################################################################################################

                     #   /***************PRODUCT ******************/

##########################################################################################################

@login_required()
def ProductList(request):

    products = Product.objects.all().order_by('-date_created')

    products = list(products)

    total_number = Product.objects.all().count

    context = {"products": products, "total_number":total_number}

    return render(request, "alldetail/products_list.html", context)

class ProductDetail(DetailView):

    templates_name = "alldetail/product_detail.html"

    model = Product

###########################################################################################################

                     #   /***************Category ******************/

##########################################################################################################

@login_required()
def CategoryList(request):

    categorys = Category.objects.all().order_by('-date_created')

    categorys = list(categorys)

    total_number = Category.objects.all().count()

    context = {"categorys": categorys}

    return render(request, "alldetail/categorys_list.html", context)

class CategoryDetail(DetailView):

    templates_name = "alldetail/category_detail.html"

    model = Category

###########################################################################################################

                     #   /***************SHOP ******************/

##########################################################################################################

@login_required()
def ShopList(request):

    shops = Shop.objects.all().order_by('-date_created')

    shops = list(shops)

    total_number = Shop.objects.all().count()

    context = {"shops": shops,"total_number":total_number}

    return render(request, "alldetail/shops_list.html", context)

class ShopDetail(DetailView):

    templates_name = "alldetail/shop_detail.html"

    model = Shop

###########################################################################################################

                     #   /***************ENTREPRISE CONVENTION CLIENT ******************/

##########################################################################################################

@login_required()
def ALLClientDataView(request):

    ALLClientDatas = ALLClientData.objects.all().order_by('-id')

    ALLClientDatas = list(ALLClientDatas)

    total_number = ALLClientData.objects.all().count()

    context = {"ALLClientDatas": ALLClientDatas, "total_number":total_number}

    return render(request, "alldetail/ALLClientData.html", context)

class DetailALLClientData(DetailView):

    templates_name = "alldetail/ALLClientData_detail.html"

    model = ALLClientData





###########################################################################################################

                      #  /***************ARTICLE  ******************/
##########################################################################################################

@login_required()
def home(request):

    article = Articles.objects.all().order_by('-date_created')

    article = list(article)

    total_number = Articles.objects.all().count()

    page = request.GET.get('page', 1)

    paginator = Paginator(article, 19)
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    context = {"articles": articles, "total_number":total_number}

    return render(request, "alldetail/index.html", context)

class ArticleDetail(DetailView):

    templates_name = "alldetail/articles_detail.html"

    model = Articles



###########################################################################################################

                     #   /*************** CART ******************/

##########################################################################################################


@login_required
def remove_favorite_article(request,article_pk):
    larticle = Articles.objects.filter(id = article_pk).first()
    user = request.user
    user.profile.articles.remove(larticle)
    user.profile.save()
    messages.success(request,"l'article {} à bien été supprimé".format(larticle.name))
    return redirect('home')



@login_required
def article_add_favorite(request,article_pk):
    larticle = Articles.objects.filter(id = article_pk).first()
    user = request.user
    if larticle in user.profile.articles.all():
       messages.warning(request,"l'article {} est déjà dans vos favoris".format(larticle))
    else:
        user.profile.articles.add(larticle)
        user.profile.save()
        messages.success(request,"l'article {} à bien été ajouter a vos favoris".format(larticle.name))
        return redirect('home')



@login_required
def mylist_article(request):
    articles = Articles.objects.filter(profile = request.user.profile)
    articles = list(articles)
    taille_mylist = len(articles)
    return render(request,"alldetail/list.html",{"articles":articles,"taille_mylist":taille_mylist})

