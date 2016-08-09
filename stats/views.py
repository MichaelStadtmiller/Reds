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
        data = ([d.wins_proj() for d in reds_data])
        for p in all_players:
            p.score = abs(int(data[0])-p.guess)
            # get next highest players guess (excluding their own)
            high = Player.objects.filter(guess__gte=p.guess).exclude(name=p.name).order_by('guess').values('guess').first()
            if high == None:    # if top, they are the highest
                high = p.guess
            else:
                high = high.values()[0]
            #TOP END: wins + games left < guess minue half way to next lowest
            #                    a. query to get next lowest number
            #                    b. average guess and next lowest
            #                    c. (wins + left) < avg; stamp it
            p.high = high
            # get next lowest players guess (excluding their own)
            low = Player.objects.filter(guess__lte=p.guess).exclude(name=p.name).order_by('-guess').values('guess').first()
            if low == None: # if bottom, they are the lowest
                p.low = p.guess
            else:
                p.low = low.values()[0]
        context['players'] = all_players
        return context

    def get_reds_data(self):
        context = {}
        reds_data = RedsData.objects.all()
        context['data'] = reds_data
        return context


class RulesView(TemplateView):
    template_name = 'stats/rules.html'
