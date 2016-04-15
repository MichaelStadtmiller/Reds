from django.views.generic import TemplateView
from .models import Player, RedsData


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
        context['players'] = all_players
        return context

    def get_reds_data(self):
        context = {}
        reds_data = RedsData.objects.all()
        context['data'] = reds_data
        return context


class RulesView(TemplateView):
    template_name = 'stats/rules.html'
