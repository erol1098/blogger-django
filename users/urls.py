from django.urls import path
from .views import  profile_page, register, user_logout, user_login

urlpatterns = [
    path('register/', register, name='register' ),
    path('logout/', user_logout, name='logout' ),
    path('login/', user_login, name='user_login'),
    path('profile/<int:id>', profile_page, name='user_profile'),
]