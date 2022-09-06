from django.urls import path, include

from blog.views import post_list

urlpatterns = [
    path('', post_list),
]
