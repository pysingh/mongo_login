from django.contrib import admin
from django.urls import path
from mainapp import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('auth/', views.auth, name='auth'),
    path('logout/', views.logout, name='logout'),
]