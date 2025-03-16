from django.shortcuts import render

# Create your views here.

from django.views.generic.detail import DetailView

from .models import event


class EventDetailView(DetailView):
    model = event
