from django.urls import path

from review import views

urlpatterns = [
    path('', views.create_review, name='add_review'),
    path('<int:id_review>', views.create_review, name='add_review'),
    path('delete_review/<int:id_review>', views.delete_review, name='delete_review'),
    path('review_with_ticket/<int:id_ticket>', views.create_review_ticket, name='review_with_ticket'),
    path('change_review/<int:id_review>', views.change_review, name='change_review'),
    path('review_with_ticket', views.create_review_ticket, name='review_with_ticket')

]
