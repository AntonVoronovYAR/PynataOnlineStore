from django.db import models
from cards.models import Card


class Cart(models.Model):
    cart_id = models.CharField(max_length=25)
    date_added = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=1)
    product = models.ForeignKey(Card, unique=False)

    class Meta:
        ordering = ['date_added']
