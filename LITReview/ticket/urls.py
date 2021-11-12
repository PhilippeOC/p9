from django.urls import path

from ticket import views

urlpatterns = [
    path('', views.create_ticket, name='add_ticket'),
    path('<int:id_ticket>', views.create_ticket, name='add_ticket'),
    path('delete_ticket/<int:id_ticket>', views.delete_ticket, name='delete_ticket'),
]
