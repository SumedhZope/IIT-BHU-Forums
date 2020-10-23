from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('testnav/', views.nav),
    path('profile/<int:id>/add_friend',views.send_friend_request),
    path('profile/<int:id>/accept_friend',views.accept_friend_request),
    path('profile/<int:id>/decline_friend',views.delete_friend_request),
    path('profile/<int:id>',views.profile),
    path('friend_requests',views.friend_request),
    path('g/<int:id>', views.group_list)
]
