from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, get_object_or_404

from review.forms import CreateReviewForm, CreateReviewTicketForm
from review.models import Review
from ticket.models import Ticket

User = get_user_model()


@login_required
def create_review(request, id_review: int = None):
    """ creation ou modification d'une critique sans répondre à un ticket """
    instance_review = get_object_or_404(Review, pk=id_review) if id_review else None

    if request.method == 'POST':
        form = CreateReviewForm(request.POST, request.FILES, instance=instance_review)
        if form.is_valid():
            instance_review = form.save(commit=False)
            instance_review.user = request.user
            if id_review is None:
                instance_review.ticket = Ticket.objects.create(title=form.cleaned_data.get('title'),
                                                               description=form.cleaned_data.get('description'),
                                                               author=request.user,
                                                               image=form.cleaned_data.get('image'))

            else:
                img_path = str(form.cleaned_data.get('image'))
                if form.cleaned_data.get('image'):
                    if img_path.count('images/') == 0:
                        img_path = 'images/' + img_path
                else:
                    img_path = None
                Ticket.objects.filter(pk=instance_review.ticket.pk).update(title=form.cleaned_data.get('title'),
                                                                           description=form.cleaned_data
                                                                                           .get('description'),
                                                                           author=request.user,
                                                                           image=img_path)

            instance_review = form.save()
            return redirect('/flux/')
    else:
        form = CreateReviewForm(instance=instance_review)
    context = {'form': form, 'title': 'Créer une critique'}
    return render(request, 'review/create_review.html', context)


@login_required
def create_review_ticket(request, id_ticket: int):
    """ creation d'une critique en réponse à un ticket """
    instance_ticket = get_object_or_404(Ticket, pk=id_ticket)
    if request.method == 'POST':
        form = CreateReviewTicketForm(request.POST, request.FILES)
        if form.is_valid():
            instance_review = form.save(commit=False)
            instance_review.user = request.user
            instance_review.title = instance_ticket.title
            instance_review.ticket_id = instance_ticket.pk
            instance_review.description = instance_ticket.description
            instance_review.image = instance_ticket.image
            instance_review.save()
            return redirect('/flux/')
    else:
        form = CreateReviewTicketForm()
    context = {'form': form, 'title': 'Créer une critique', 'ticket': instance_ticket}
    return render(request, 'review/create_review_ticket.html', context)


@login_required
def change_review(request, id_review: int):
    """ modification d'une critique """
    instance_review = get_object_or_404(Review, pk=id_review)
    instance_ticket = Ticket.objects.get(review__pk=id_review)

    if instance_review.user == User.objects.get(pk=instance_ticket.author_id):
        form = CreateReviewForm(instance=instance_review)
        context = {'form': form, 'title': 'Modifier une critique'}
        return render(request, 'review/create_review.html', context)
    else:
        if request.method == 'POST':
            form = CreateReviewTicketForm(request.POST, request.FILES, instance=instance_review)
            if form.is_valid():
                instance_review = form.save(commit=False)
                instance_review.title = instance_review.title
                instance_review.description = instance_review.description
                instance_review.image = instance_review.image
                instance_review.save()
                return redirect('/flux/')

        instance_ticket = Ticket.objects.get(review__pk=id_review)
        instance_ticket.author = User.objects.get(ticket__pk=instance_ticket.id)

        form = CreateReviewTicketForm(instance=instance_review)
        context = {'form': form, 'title': 'modifier une critique', 'ticket': instance_ticket}
        return render(request, 'review/create_review_ticket.html', context)


@login_required
def delete_review(request, id_review: int):
    """ supprime une critique """
    review = get_object_or_404(Review, pk=id_review)
    review.delete()
    return redirect('/flux/')
