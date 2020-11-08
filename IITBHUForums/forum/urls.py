from django.contrib import admin
from django.urls import path,include
from . import views
from .models import Group

urlpatterns = [
    path('testnav/', views.nav, name='navbar'),
    path('groups/new_group/',views.submit_form,name="new_group"),
    path('new_post/', views.make_post),
    path('groups/',views.groups,name = 'groups'),
    path('profile/',views.profile),
    path( 'group/<int:id>/' ,views.group_home,name='group_home')
]