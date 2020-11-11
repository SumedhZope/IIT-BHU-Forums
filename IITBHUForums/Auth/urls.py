from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.landingpage, name='homepage'),
    path('logout/', views.logout_func),
  #  path('friends/', views.friends_list)
]
