from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('profile/', views.profile),
    path('login/', views.loginpage),
    path('register/',views.register),
]
