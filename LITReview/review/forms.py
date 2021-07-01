
from django import forms


from review.models import Review

RANKING_CHOICES = [
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    ]


class CreateReviewForm(forms.ModelForm):
    """ Formulaire permettant de créer un ticket et une critique simultanément """
    rating = forms.ChoiceField(label='Note', widget=forms.RadioSelect(), choices=RANKING_CHOICES)

    class Meta:
        model = Review
        fields = ['title', 'description', 'image', 'headline', 'rating', 'body']
        labels = {
            'title': 'Titre',
            'description': 'Description',
            'headline': 'Titre',
            'rating': 'Note',
            'body': 'Commentaire',
        }


class CreateReviewTicketForm(forms.ModelForm):
    """ Formulaire de création d'une critique en réponse à un ticket """
    rating = forms.ChoiceField(label='Note', widget=forms.RadioSelect(), choices=RANKING_CHOICES)

    class Meta:
        model = Review
        fields = ['headline', 'rating', 'body']
        labels = {
            'headline': 'Titre',
            'rating': 'Note',
            'body': 'Commentaire',
        }
