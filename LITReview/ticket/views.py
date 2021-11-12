from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, get_object_or_404

from ticket.forms import CreateTicketForm
from ticket.models import Ticket

User = get_user_model()


@login_required
def create_ticket(request, id_ticket: int = None):
    """ creation et modification d'un ticket """
    instance_ticket = get_object_or_404(Ticket, pk=id_ticket) if id_ticket else None
    if request.method == 'POST':
        form = CreateTicketForm(request.POST, request.FILES, instance=instance_ticket)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.author = request.user
            ticket = form.save()
            return redirect('/flux/')
    else:
        form = CreateTicketForm(instance=instance_ticket)
    context = {'form': form, 'title': 'Créer un ticket'}
    return render(request, 'ticket/create_ticket.html', context)


@login_required
def delete_ticket(request, id_ticket: int):
    """ supprime un ticket """
    ticket = get_object_or_404(Ticket, pk=id_ticket)
    ticket.delete()
    return redirect('/flux/')
