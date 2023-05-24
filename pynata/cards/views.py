from django.shortcuts import render
from .models import Card


def index(request):
    template = 'index.html'
    cards = Card.objects.all()
    context = {
        'cards': cards
    }
    return render(request, template, context)
