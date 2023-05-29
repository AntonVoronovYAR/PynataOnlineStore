import requests
import os
from dotenv import load_dotenv

load_dotenv()
CONDITION_STATUS: dict = {
    'clear': 'Ясно',
    'partly-cloudy': 'Малооблачно',
    'cloudy': 'Облачно с прояснениями',
    'overcast': 'Пасмурно',
    'drizzle': 'Морось',
    'light-rain': 'Небольшой дождь',
    'rain': 'Дождь',
    'moderate-rain': 'Умеренно сильный дождь',
    'heavy-rain': 'Сильный дождь',
    'continuous-heavy-rain': 'Длительный сильный дождь',
    'showers': 'Ливень',
    'wet-snow': 'Дождь со снегом',
    'light-snow': 'Небольшой снег',
    'snow': 'Снег',
    'snow-showers': 'Снегопад',
    'hail': 'Град',
    'thunderstorm': 'Гроза',
    'thunderstorm-with-rain': 'Дождь с грозой',
    'thunderstorm-with-hail': 'Гроза с градом',
}


def get_weather_data() -> dict:
    """Запрос данных от API Яндекс погоды."""
    url = 'https://api.weather.yandex.ru/v2/informers'
    key = str(os.getenv('YANDEX_WEATHER_KEY'))
    headers = {'X-Yandex-API-Key': key}
    params = {'lat': 57.626559, 'lon': 39.893813}
    weather_data = requests.get(url, headers=headers, params=params)
    return weather_data.json()


def parse_data(data: dict) -> dict:
    """Извлечение необходимых данных."""
    weather = {
        'temperature': data['fact']['temp'],
        'condition': CONDITION_STATUS[data['fact']['condition']],
        'icon': data['fact']['icon']
    }
    return weather


def main(request):
    data = get_weather_data()
    weather = parse_data(data)
    return {'weather': weather}

