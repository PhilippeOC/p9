from django.urls import path

from userfollows import views

urlpatterns = [
    path('', views.display_users, name='userfollows'),
]
