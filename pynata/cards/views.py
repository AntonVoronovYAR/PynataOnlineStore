from django.shortcuts import render
from .models import Card
from api.abroad_api import yandex_weather


def index(request):
    template = 'index.html'
    cards = Card.objects.all()
    weather_data = yandex_weather.get_weather_data()
    temperature, condition, icon = yandex_weather.parse_data(weather_data)
    context = {
        'cards': cards,
        'temp': temperature,
        'cond': condition,
        'icon': icon,
    }
    return render(request, template, context)
