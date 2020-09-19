from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    #path('login/', views.loginpage),
    #path('register/',views.register),
    path('', views.landingpage, name='homepage'),
    path('logout/', views.logout_func)
]
