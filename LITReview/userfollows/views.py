from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model

from userfollows.models import UserFollows
from userfollows.forms import CreateFollowerForm

User = get_user_model()


@login_required
def display_users(request):

    form = create_followers(request)

    users_following = []
    for user_following in request.user.following.all():
        users_following.append(User.objects.get(pk=user_following.followed_user_id))

    followed_users = []
    for followed_user in request.user.followed_by.all():
        followed_users.append(User.objects.get(pk=followed_user.user_id))

    users = User.objects.all()

    context = {'users': users,
               'form': form,
               'users_following': users_following,
               'followed_users': followed_users,
               "title": 'Abonement'}
    return render(request, 'userfollows/view_userfollows.html', context)


@login_required
def create_followers(request):
    if request.method == "POST":
        form = CreateFollowerForm(user=request.user, data=request.POST)
        if form.is_valid():
            follow = form.cleaned_data.get('user_to_follow')
            UserFollows.objects.create(user=request.user, followed_user=User.objects.get(username=follow))
    else:
        form = CreateFollowerForm(user=request.user)
    return form


@login_required
def delete_follower(request, id_follow=None):
    UserFollows.objects.filter(followed_user_id=id_follow, user_id=request.user.id).delete()
    return redirect('/flux/')
