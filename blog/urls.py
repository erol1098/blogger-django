from django.urls import path, include

from .views import post_create, post_delete, post_detail, post_list, post_update, like_post

urlpatterns = [
    path('', post_list, name="index"),
    path('add/', post_create, name="add"),
    path('detail/<int:id>', post_detail, name="datail"),
    path('update/<int:id>', post_update, name="update"),
    path('delete/<int:id>', post_delete, name="delete"),
    path('like/<int:id>', like_post, name="like"),
]
