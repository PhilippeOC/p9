
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
# from django.contrib.auth import get_user_model


def index(request):
    return render(request, 'user/index.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        # if form.is_valid():
        #     form.save()
        #     username = form.cleaned_data['username']
        #     password = form.cleaned_data['password']
        #     usr = authenticate(username=username, password=password)
        #     login(request, usr)
        #     return redirect('index')

    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', locals())
