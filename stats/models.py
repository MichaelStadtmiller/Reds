from __future__ import unicode_literals
from django.db import models


# Create your models here.
class Player(models.Model):
    Name = models.CharField(max_length=20, primary_key=True)
    Guess = models.IntegerField(default=0)

    def __getitem__(self, item):
        return getattr(self, item)

    def __str__(self):
        return self.Name + " " + str(self.Guess)


class RedsData(models.Model):
    played = models.IntegerField(default=0)
    won = models.IntegerField(default=0)
    lost = models.IntegerField(default=0)

    def games_left(self):
        total_games = 162
        return total_games - self.played
