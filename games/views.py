from django.shortcuts import render

from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Game


# Create your views here.
class gameListView(ListView):
    template_name = 'games/games_list.html'
    model = Game


class gameDetailView(DetailView):
    template_name = 'games/game_detail.html'
    model = Game


class gameCreateView(CreateView):
    template_name = 'games/game_create.html'
    model = Game
    fields = ['name', 'rate', 'desc']


class gameUpdateView(UpdateView):
    template_name = 'games/game_update.html'
    model = Game
    fields = ['name', 'rate', 'desc']


class gameDeleteView(DeleteView):
    template_name = 'games/game_delete.html'
    model = Game
    success_url = reverse_lazy('games_list')
