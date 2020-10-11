from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.submit_form, name='groups'),
]
