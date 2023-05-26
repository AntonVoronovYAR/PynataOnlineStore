from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Card
from .forms import FeedbackForm
from api.abroad_api import yandex_weather


def index(request):
    template = 'index.html'
    cards = Card.objects.all()
    weather_data = yandex_weather.get_weather_data()
    weather = yandex_weather.parse_data(weather_data)
    context = {
        'cards': cards,
        'weather': weather,
    }
    return render(request, template, context)


def card_detail(request, card_id):
    card = get_object_or_404(Card, id=card_id)
    feedback_form = FeedbackForm()
    context = {
        'card': card,
        'feedback_form': feedback_form,
        'feedbacks': card.feedbacks.all(),
    }
    return render(request, 'cards/card_detail.html', context)


@login_required
def add_feedback(request, card_id):
    card = get_object_or_404(Card, id=card_id)
    form = FeedbackForm(request.POST or None)
    if form.is_valid():
        feedback = form.save(commit=False)
        feedback.author = request.user
        feedback.card = card
        feedback.save()
    return redirect('cards:card_detail', card_id=card_id)
