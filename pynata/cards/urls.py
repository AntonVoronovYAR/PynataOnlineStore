from django.urls import path

from . import views

app_name = 'cards'

urlpatterns = [
    path('', views.index, name='main_page'),
    # path('card/', views.card_list, name='card_list'),
    path('card/<int:card_id>/', views.card_detail, name='card_detail'),
    path('card/<int:card_id>/feedback/',
         views.add_feedback, name='add_feedback'),
]
