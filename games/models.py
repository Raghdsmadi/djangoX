from django.db import models
from django.db import models
from django.urls import reverse

from accounts.models import CustomUser


class Game(models.Model):
    name = models.CharField(max_length=256)
    rate = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    desc = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('games_list')
