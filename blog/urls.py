from django.urls import path, include

from .views import post_create, post_list

urlpatterns = [
    path('', post_list, name="index"),
    path('add/', post_create, name="add"),
]
