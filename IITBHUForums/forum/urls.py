from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('feed/', views.feed),
    path('profile/',views.profile),
    path('g/<int:id>', views.group_list)
]
