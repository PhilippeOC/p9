
from django.contrib.auth import forms as auth_form

from django.contrib.auth import get_user_model

User = get_user_model()


class CreateUserForm(auth_form.UserCreationForm):
    """ formulaire d'inscription """
    class Meta(auth_form.UserCreationForm.Meta):
        model = User
        fields = ['username', 'password1', 'password2']
