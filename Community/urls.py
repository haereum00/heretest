# community/urls.py
from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('', views.community_home, name='home'),
    path('followers/', views.follower_list, name='follower_list'),
    path('following/', views.following_list, name='following_list'),
]
