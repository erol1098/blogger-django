from django.urls import path, include

from .views import post_create, post_delete, post_list, post_update

urlpatterns = [
    path('', post_list, name="index"),
    path('add/', post_create, name="add"),
    path('update/<int:id>', post_update, name="update"),
    path('delete/<int:id>', post_delete, name="delete"),
]
