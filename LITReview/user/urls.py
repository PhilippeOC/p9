from django.urls import path
# from django.contrib.auths import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('profile_user', views.profile_user, name='profile_user'),
    
]
