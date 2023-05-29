from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

MAX_TEXT_LEN: int = 15

TYPE_OF_SIZES: tuple = (
    ('S', 'S'),
    ('M', 'M'),
    ('L', 'L'),
    ('Xl', 'XL'),
)

TYPE_OF_PYNATA: tuple = (
    ('Circle', 'Круглая'),
    ('Shield', 'Щит'),
    ('Figure', 'Фигурная'),
)

RATINGS = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5)
)


class Filling(models.Model):
    """Наполнение Пиньяты."""
    name = models.CharField(max_length=50, help_text='Наименование')
    description = models.TextField(help_text='Описание')
    size_type = models.CharField(choices=TYPE_OF_SIZES, max_length=50, help_text='Тип наполнения')
    weigth = models.IntegerField(help_text='Вес в гр.')
    cost = models.IntegerField(help_text='Цена')
    image = models.ImageField(
        upload_to='card/',
        help_text='Картинка',
    )

    def __str__(self):
        return self.name


class Card(models.Model):
    """Карточка Пиньяты."""
    name = models.CharField(max_length=50, help_text='Наименование')
    description = models.TextField(help_text='Описание')
    pynata_type = models.CharField(choices=TYPE_OF_PYNATA, max_length=50, help_text='Форма')
    size_type = models.CharField(choices=TYPE_OF_SIZES, max_length=50, help_text='Размер')
    cost = models.IntegerField(help_text='Цена')
    filling = models.ForeignKey(
        Filling,
        null=True,
        help_text='Наполнение',
        on_delete=models.CASCADE,
        related_name='cards',
    )
    image = models.ImageField(
        upload_to='card/',
        help_text='Картинка',
    )

    def __str__(self):
        return self.name[:MAX_TEXT_LEN]


class Service(models.Model):
    """Карточка услуги."""
    name = models.CharField(max_length=50, help_text='Наименование')
    cost = models.IntegerField(help_text='Цена')
    image = models.ImageField(
        upload_to='card/',
        help_text='Картинка',
    )

    def __str__(self):
        return self.name[:MAX_TEXT_LEN]


class Feedback(models.Model):
    """Отзывы."""
    card = models.ForeignKey(
        Card,
        blank=True,
        null=False,
        on_delete=models.CASCADE,
        related_name='feedbacks',
        help_text='Карточка товара'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        related_name='feedbacks',
        help_text='Пользователь'
    )
    text = models.TextField(help_text='Текст отзыва')
    rating = models.IntegerField(
        choices=RATINGS,
        null=True,
        help_text='Рейтинг'
    )
    created = models.DateTimeField(auto_now_add=True, help_text='Дата отзыва')

    def __str__(self):
        return f'{self.author}: {self.text[:MAX_TEXT_LEN]}'


