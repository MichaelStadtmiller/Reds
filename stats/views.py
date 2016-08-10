from django.views.generic import TemplateView
from .models import Player, RedsData
from django.db.models import Func, F

class MainView(TemplateView):
    template_name = 'stats/index.html'

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context['all_players'] = self.get_all_players
        context['reds_data'] = self.get_reds_data
        return context

    def get_all_players(self):
        context = {}
        all_players = Player.objects.all()
        reds_data = RedsData.objects.all()
        # data = ([d.wins_proj() for d in reds_data])
        for d in reds_data:
            data = [d.wins_proj()]
        for p in all_players:
            # calculate player's score
            p.score = abs(int(data[0])-p.guess)
            ## LOWER LIMIT ##
            # get next highest guess (excluding their own)
            above = Player.objects.filter(guess__gt=p.guess).order_by('guess').values('guess').first()
            if above == None:    # if top, they are the highest
                above = p.guess
            else:
                above = above.values()[0]
            p.above = above #DEBUG - REMOVE
            # use players guess and next highest to calculate a limit. Any wins > limit = GONE
            p.lower_limit = (p.guess + above)/2

            ## UPPER LIMIT ##
            # get next lowest players guess (excluding their own)
            below = Player.objects.filter(guess__lt=p.guess).order_by('-guess').values('guess').first()
            if below == None: # if bottom, they are the lowest
                below = p.guess
            else:
                below = below.values()[0]
            p.below = below #DEBUG - REMOVE
            # user players' guess and next lowest to calculate an upper limit. Any wins < limit = GONE
            p.upper_limit = (p.guess + below)/2
        context['players'] = all_players
        return context

    def get_reds_data(self):
        context = {}
        reds_data = RedsData.objects.all()
        context['data'] = reds_data
        return context


class RulesView(TemplateView):
    template_name = 'stats/rules.html'
