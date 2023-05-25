from django.shortcuts import render
from .models import Card
from ..api.abroad_api import yandex_weather


def index(request):
    template = 'index.html'
    cards = Card.objects.all()
    context = {
        'cards': cards

    }
    return render(request, template, context)
