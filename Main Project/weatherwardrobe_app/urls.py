from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('base.html', views.home, name='base'),
    path('register.html', views.register, name='register'),
    path('login.html', views.login, name='login'),
]