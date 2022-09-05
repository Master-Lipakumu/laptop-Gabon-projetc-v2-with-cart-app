
from django.urls import path, include

from .views import *

urlpatterns = [
    # allclient
    path('client', allclient, name="client"),
    path("search/", SearchResultsView.as_view(), name="search_results"),
    #path('api/', include(router.urls)),
    path('', home, name="home"),
    path('<int:pk>/', ArticleDetail.as_view(), name="articles-detail"),
    path('article_form', ArticleCreateView.as_view(), name="articles-created"),
    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name="articles-updated"),
    path('<int:pk>/edit/staff/', ArticleStaffUpdateView.as_view(), name="articles-updated-staff"),
    # convention client
    path('allclientdata', ALLClientDataView, name="allclientdata"),
    path('allclientdataupdateview/edit/<int:pk>/', ALLClientDataUpdateView.as_view(), name="allclientdataupdateview"),
    path('detailallclientdata/<int:pk>/', DetailALLClientData.as_view(), name="detailallclientdata"),
    path('allclientdatacreateview', ALLClientDataCreateView.as_view(), name="allclientdatacreateview"),
    # magazin
    path('shop', ShopList, name="Shop"),
    path('shop/<int:pk>/', ShopDetail.as_view(), name="shop-detail"),
    path('shop_form', ShopCreateView.as_view(), name="shop-created"),
    path('shop/<int:pk>/edit/', ShopUpdateView.as_view(), name="shop-update"),
    # category
    path('category', CategoryList, name="category"),
    path('category/<int:pk>/', CategoryDetail.as_view(), name="category-detail"),
    path('category_form', CategoryCreateView.as_view(), name="category-created"),
    path('category/<int:pk>/edit/', CategoryUpdateView.as_view(), name="category-updated"),
    
    #produit 
    path('product', ProductList, name="product"),
    path('product/<int:pk>/', ProductDetail.as_view(), name="product-detail"),
    path('product_form', ProductCreateView.as_view(), name="product-created"),
    path('product/<int:pk>/edit/', ProductUpdateView.as_view(), name="product-updated"),

    path('article_add_favorite/<int:article_pk>', article_add_favorite, name="article_add_favorite"),
    path('remove_favorite_article/<int:article_pk>', remove_favorite_article, name="remove_favorite_article"),
    path('mylist/', mylist_article, name="mylist_article"),
    
   
]
