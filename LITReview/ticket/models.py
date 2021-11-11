from django.db import models
from django.utils import timezone
from django.apps import apps
from django.contrib.auth import get_user_model

User = get_user_model()


class Ticket(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2048)
    time_created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images', null=True, blank=True)

    def __str__(self) -> str:
        """ affiche le titre du ticket et la date de sa création dans l'admin """
        return self.title + ' - ' + str(timezone.localtime(self.time_created).strftime('le %d-%m-%Y à %H:%M:%S'))

    def has_review(self) -> bool:
        """ retourne True si le ticket à un avis"""
        return bool(apps.get_model('review', 'Review').objects.filter(ticket=self))
