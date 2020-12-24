from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register.html', views.register, name='register'),
    path('login.html', views.login, name='login'),
]