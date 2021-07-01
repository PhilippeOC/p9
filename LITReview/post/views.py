from django.contrib.auth.decorators import login_required
from django.db.models import CharField, Value
from django.shortcuts import render

from itertools import chain
from ticket.models import Ticket
from review.models import Review


@login_required
def display_posts(request):
    """ Affiche tous les posts de l'utilisateur connecté """
    tickets = Ticket.objects.filter(author=request.user)
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))
    reviews = Review.objects.filter(user=request.user)
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))
    posts = sorted(
        chain(reviews, tickets),
        key=lambda post: post.time_created,
        reverse=True
    )
    context = {'posts': posts, 'title': 'Posts'}
    return render(request, 'post/view_post.html', context)

    
