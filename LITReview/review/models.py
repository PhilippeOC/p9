from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

from ticket.models import Ticket

User = get_user_model()

class Review(models.Model):
    ticket = models.ForeignKey(Ticket, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2048)
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    time_created = models.DateTimeField(auto_now_add=True, null=True)
    headline = models.CharField(max_length=128)
    body = models.TextField(max_length=8192, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images', null=True, blank=True)

    def __str__(self):
        return self.headline + ' - ' + str(timezone.localtime(self.time_created).strftime('le %d-%m-%Y à %H:%M:%S'))