from django.contrib import admin
from django.urls import path
from mainapp import views

urlpatterns = [
    path('login/', views.login),
    path('home/', views.home, name='home'),
]