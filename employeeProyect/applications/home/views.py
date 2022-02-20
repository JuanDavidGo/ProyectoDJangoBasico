from re import template
from django.shortcuts import render

from django.views.generic import TemplateView, ListView

# Create your views here.
class HomeView(TemplateView):
    template_name = ''


class PruebaListView(ListView):
    template_name = "home/list.html"
    context_object_name = 'listaNumeros'
    queryset = ['1','2','3']

