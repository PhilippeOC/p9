from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import CreateUserForm


def home(request):
    if request.user.is_authenticated:
        return redirect('/flux/')
    return redirect('login/')


def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username}, votre compte a été créé. Vous pouvez vous connecter.')
            form.save()
            return redirect('home')
    else:
        form = CreateUserForm()
    context = {'form': form, 'title': 'Inscription'}
    return render(request, 'user/register.html', context)
