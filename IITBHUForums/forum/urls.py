from django.contrib import admin
from django.urls import path,include
from . import views
from .models import Group

urlpatterns = [
    path('feed/', views.feed, name="feed"),
    path('search/', views.search, name="search"),
    path('profile/<int:id>/add_friend',views.send_friend_request),
    path('profile/<int:id>/accept_friend',views.accept_friend_request),
    path('profile/<int:id>/decline_friend',views.delete_friend_request),
    path('profile/<int:id>',views.profile),
    path('friend_requests',views.friend_request),
    path('p/<int:id>',views.post_view,name="post_view"),
    path('groups/new_group/',views.submit_form,name="new_group"),
    path('new_post/', views.make_post),
    path('groups/',views.groups,name = 'groups'),
    path('group/<int:id>/' ,views.group_home,name='group_home'),
    path('group/<int:id>/members', views.member_list, name='member_list'),
    path('group/<int:id>/add_role', views.add_role, name="add_role")
]

