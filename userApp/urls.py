from django.contrib import admin
from django.urls import path, include

from userApp import views

urlpatterns = [
    path('getRegister/', views.getRegister),
    path('getMap/', views.getMap),
    path('login/', views.login),
    path('arrive/', views.arrive_login),
]
