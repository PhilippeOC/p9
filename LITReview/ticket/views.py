from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, get_object_or_404

from ticket.forms import CreateTicketForm
from ticket.models import Ticket

User = get_user_model()


@login_required
def create_ticket(request, id_ticket=None):
    """ creation et modification d'un ticket """
    instance_ticket = get_object_or_404(Ticket, pk=id_ticket) if id_ticket is not None else None
    if request.method == 'POST':
        form = CreateTicketForm(request.POST, request.FILES, instance=instance_ticket)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.author = request.user
            ticket = form.save()
            return redirect('view_ticket')
    else:
        form = CreateTicketForm(instance=instance_ticket)
    context = {'form': form, 'title': 'Créer un ticket'}
    return render(request, 'ticket/create_ticket.html', context)


@login_required
def display_tickets(request):
    """ affiche tous les tickets par ordre chronologique inversé """
    tickets = Ticket.objects.order_by('-time_created')
    # tickets = Ticket.objects.all()
    return render(request, 'ticket/view_ticket.html', locals())


@login_required
def delete_ticket(request, id_ticket):
    """ supprime un ticket """
    ticket = get_object_or_404(Ticket, pk=id_ticket)
    ticket.delete()
    return redirect('view_ticket')

# def disp_user(request):
#     auteurs = User.objects.filter(username=request.user).first()
#     print('auteur', auteurs)
#     print('connected', request.user)
#     return render(request, 'ticket/view_ticket.html', locals())
