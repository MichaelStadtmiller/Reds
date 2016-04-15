from django.conf.urls import url
from django.views.generic.base import RedirectView
from .views import *

urlpatterns = [
    url(r'^$', MainView.as_view(), name='index'),
    url(r'^rules$', RulesView.as_view(), name='rules'),
]