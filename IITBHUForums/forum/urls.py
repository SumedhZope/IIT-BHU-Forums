from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('testnav/', views.nav, name='navbar'),
    path('p/<int:id>',views.post_view,name="post_view"),
    path('groups/new_group/',views.submit_form,name="new_group"),
    path('new_post/', views.make_post),
    path('groups/',views.groups,name = 'groups'),
    path('profile/',views.profile)

