from django.contrib import admin
from .models import Card, Filling


class CardsAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'pynata_type',
        'size_type',
        'filling',
        'cost',
        'image',
    )
    list_editable = (
        'name',
        'pynata_type',
        'size_type',
        'filling',
        'cost',
        'image',
    )
    search_fields = ('name', 'cost',)
    list_filter = ('name', 'cost',)
    empty_value_display = '-пусто-'


admin.site.register(Card, CardsAdmin)
admin.site.register(Filling)

