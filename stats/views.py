from django.shortcuts import render
from .models import Player, RedsData
# Create your views here.


def index(request):
    return render(request, 'stats/index.html')


def rules(request):
    return render(request, 'stats/rules.html')
