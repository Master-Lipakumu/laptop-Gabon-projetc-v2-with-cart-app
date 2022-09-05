from django.urls import path, include
from .views import profile, register, login, logout, users, UsersDetail

urlpatterns = [
    path('', profile, name="profile"),
    path('users/', users, name="users"),
    path('users/<int:pk>/', UsersDetail.as_view(), name="users-detail"),
    path('register/', register, name="register"),
    path('login/', login, name="login"),
    path('logout/', logout,name="logout"),
]