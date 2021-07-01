from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import get_user_model

User = get_user_model()


@login_required
def display_users(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'userfollows/view_userfollows.html', context)
