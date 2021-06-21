from django.forms import ModelForm

from ticket.models import Ticket


class CreateTicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image']
        labels = {
            'title': 'Titre',
            'description': 'Description',
        }
