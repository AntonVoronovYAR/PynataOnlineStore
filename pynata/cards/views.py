from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from .models import Card
from .forms import FeedbackForm


def index(request):
    template = 'index.html'
    cards = Card.objects.all()
    context = {
        'cards': cards,
    }
    return render(request, template, context)


def card_detail(request, card_id):
    card = get_object_or_404(Card, id=card_id)
    rating = Card.objects.annotate(
        rating=Avg('feedbacks__rating')).get(pk=card_id).rating
    feedback_form = FeedbackForm()
    context = {
        'card': card,
        'feedback_form': feedback_form,
        'feedbacks': card.feedbacks.all(),
        'rating': round(rating, 1)
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
