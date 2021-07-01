from django.contrib.auth.decorators import login_required
from django.db.models import CharField, Value
from django.shortcuts import render

from itertools import chain
from ticket.models import Ticket
from review.models import Review


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
    return Review.objects.all()


def get_users_viewable_tickets(request):
    return Ticket.objects.all()
