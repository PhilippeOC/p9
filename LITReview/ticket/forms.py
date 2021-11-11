from django.forms import ModelForm

from ticket.models import Ticket


class CreateTicketForm(ModelForm):
    """ formulaire de création d'un ticket """
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image']
        labels = {
            'title': 'Titre',
            'description': 'Description',
        }
