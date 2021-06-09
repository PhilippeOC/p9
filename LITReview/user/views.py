
from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import authenticate, login
from django.contrib import messages
# from django.contrib.auth import get_user_model
from .forms import CreateUserForm


def home(request):
    return render(request, 'user/home.html')


def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username}, votre compte à été créé. Vous pouvez vous connecter.')
            # form.save()
            return redirect('login')
    else:
        form = CreateUserForm()
    context = {'form': form, 'title': 'Inscription'}
    return render(request, 'user/register.html', context)


def profile_user(request):
    context = {'title': 'Profil'}
    return render(request, 'user/profile_user.html', context)

