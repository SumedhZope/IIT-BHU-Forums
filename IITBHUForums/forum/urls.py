from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('feed/', views.feed, name="feed"),
    path('profile/<int:id>/add_friend',views.send_friend_request),
    path('profile/<int:id>/accept_friend',views.accept_friend_request),
    path('profile/<int:id>/decline_friend',views.delete_friend_request),
    path('profile/<int:id>',views.profile),
    path('friend_requests',views.friend_request),
    path('p/<int:id>',views.post_view,name="post_view"),
    path('groups/new_group/',views.submit_form,name="new_group"),
    path('new_post/', views.make_post),
    path('groups/',views.groups,name = 'groups'),
]
