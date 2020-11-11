from django.contrib import admin
from django.urls import path,re_path
from .views import ThreadView

urlpatterns = [
    path("<str:username>/", ThreadView),
]