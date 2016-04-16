from __future__ import unicode_literals, division
from django.db import models


# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=20, primary_key=True)
    guess = models.IntegerField(default=0)

    def total_games(self):
        return 162

    def perc_guess(self):
        return self.guess/self.total_games()*100

    def __getitem__(self, item):
        return getattr(self, item)

    def __str__(self):
        return self.name + " " + str(self.guess)


class RedsData(models.Model):
    lastGamePlayed = models.DateField(primary_key=True)
    won = models.IntegerField(default=0)
    lost = models.IntegerField(default=0)
    total_games = 162

    def games_played(self):
        return self.won+self.lost

    def games_left(self):
        return self.total_games - self.games_played()

    def perc_won(self):
        return self.won/self.total_games*100

    def perc_lost(self):
        return self.lost/self.total_games*100

    def perc_left(self):
        return self.games_left()/self.total_games*100

    def currwinrate(self):
        return int(round(self.won/self.games_played()*100))

    def wins_proj(self):
        return int(self.total_games*(self.currwinrate()/100))

    def __str__(self):
        return str(self.lastGamePlayed) + " (" + str(self.won) + "-" + str(self.lost) + ")"
