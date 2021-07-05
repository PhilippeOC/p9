from django.contrib.auth.decorators import login_required
from django.db.models import CharField, Value
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist

from itertools import chain
from ticket.models import Ticket
from review.models import Review
from userfollows.models import UserFollows

User = get_user_model()


@login_required
def display_flux(request):
    reviews = get_users_viewable_reviews(request.user)
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))

    tickets = get_users_viewable_tickets(request.user)
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))

    posts = sorted(
        chain(reviews, tickets),
        key=lambda post: post.time_created,
        reverse=True
    )

    return render(request, 'flux/view_flux.html', context={'posts': posts})


def get_users_viewable_reviews(request):
    """ retourne les reviews aux tickets des auteurs auxquels l'utilisateur connecté est abonné """
    subscription_list = [User.objects.get(username=request.username).id]
    for user_following in UserFollows.objects.filter(user_id=User.objects.get(username=request.username).id):
        subscription_list.append(user_following.followed_user_id)
    review_id_list = []
    for ticket in Ticket.objects.filter(author_id__in=subscription_list):
        try:
            review_id_list.append(Review.objects.get(ticket_id=ticket.id).id)
        except ObjectDoesNotExist:
            continue
    return Review.objects.filter(id__in=review_id_list)


def get_users_viewable_tickets(request):
    """ retourne les tickets des auteurs auxquels l'utilisateur connecté est abonné """
    subscription_list = [User.objects.get(username=request.username).id]
    for user_following in UserFollows.objects.filter(user_id=User.objects.get(username=request.username).id):
        subscription_list.append(user_following.followed_user_id)
    return Ticket.objects.filter(author_id__in=subscription_list)
