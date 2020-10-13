from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('testnav/', views.nav, name='navbar'),
    path('new_group/',views.submit_form,name="new_group")
]
