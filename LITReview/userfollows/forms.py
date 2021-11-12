from django import forms
from django.contrib.auth import get_user_model

from userfollows.models import UserFollows


User = get_user_model()


class CreateFollowerForm(forms.ModelForm):
    """ formulaire d'abonnement pour suivre un utilisateur """
    class Meta:
        model = UserFollows
        fields = ['user_to_follow']
        labels = {'user_to_follow': "Nom d'utilisateur"}

    def __init__(self, user, *args, **kwargs):
        """ recupère l'utilisateur connecté"""
        self.user = user
        super().__init__(*args, **kwargs)

    def clean_user_to_follow(self):
        """ vérifie la validité de l'utilisateur à suivre"""
        user_to_follow = self.cleaned_data.get('user_to_follow')

        if User.objects.filter(username=user_to_follow):
            if UserFollows.objects.filter(followed_user_id=User.objects.get(username=user_to_follow),
                                          user_id=self.user):
                raise forms.ValidationError(f"Vous suivez déjà les publications de {user_to_follow}")
            return user_to_follow
        else:
            raise forms.ValidationError("Le nom d'utilisateur n'est pas valide")
