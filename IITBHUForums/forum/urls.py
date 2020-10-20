from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('testnav/', views.nav),
    path('profile/',views.profile),
    path('g/<int:id>', views.group_list)
]
