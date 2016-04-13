from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext, loader
from .models import Player, RedsData

#def index(request):
#    return render(request, 'stats/index.html')


def index(request):
    all_players = Player.objects.all()
    template = loader.get_template('stats/index.html')
    context = RequestContext(request, {'all_players': all_players, },)
    return HttpResponse(template.render(context))


def rules(request):
    return render(request, 'stats/rules.html')
