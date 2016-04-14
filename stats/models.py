from __future__ import unicode_literals
from django.db import models
from datetime import datetime


# Create your models here.
class Player(models.Model):
    Name = models.CharField(max_length=20, primary_key=True)
    Guess = models.IntegerField(default=0)

    def __getitem__(self, item):
        return getattr(self, item)

    def __str__(self):
        return self.Name + " " + str(self.Guess)


class RedsData(models.Model):
    lastGamePlayed = models.DateField(primary_key=True)
    won = models.IntegerField(default=0)
    lost = models.IntegerField(default=0)

    #def total_games(self):
    #    return 162

    def games_played(self):
        return self.won+self.lost

    def games_left(self):
        total_games = 162
        #return self.total_games() - self.games_played()
        return total_games - self.games_played()

    def __str__(self):
        return str(self.lastGamePlayed) + " (" + str(self.won) + "-" + str(self.lost) + ")"
