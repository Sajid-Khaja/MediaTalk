from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('tweet/',views.tweet_list,name='tweet_list'),
    path('',views.index,name='index'),
    path('create/',views.tweet_create,name='tweet_create'),
    path('<int:tweet_id>/edit/',views.tweet_edit,name='tweet_edit'),
    path('<int:tweet_id>/delete/',views.tweet_delete,name='tweet_delete'),
    path('register/',views.register,name='register'),
    path('search/', views.search_users, name='search_users'),
    
]  