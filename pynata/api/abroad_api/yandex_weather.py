import requests
import os
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()

CONDITION_STATUS = {
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
d = {'fact': {'condition': 'overcast',
              'daytime': 'd',
              'feels_like': 20,
              'humidity': 73,
              'icon': 'ovc',
              'obs_time': 1685019600,
              'polar': False,
              'pressure_mm': 752,
              'pressure_pa': 1002,
              'season': 'spring',
              'temp': 19,
              'wind_dir': 'e',
              'wind_gust': 4.6,
              'wind_speed': 1},
     'forecast': {'date': '2023-05-25',
                  'date_ts': 1684962000,
                  'moon_code': 11,
                  'moon_text': 'moon-code-11',
                  'parts': [{'condition': 'rain',
                             'daytime': 'd',
                             'feels_like': 17,
                             'humidity': 92,
                             'icon': 'ovc_ra',
                             'part_name': 'evening',
                             'polar': False,
                             'prec_mm': 0.8,
                             'prec_period': 240,
                             'prec_prob': 90,
                             'pressure_mm': 752,
                             'pressure_pa': 1002,
                             'temp_avg': 17,
                             'temp_max': 17,
                             'temp_min': 16,
                             'wind_dir': 'nw',
                             'wind_gust': 3.2,
                             'wind_speed': 2.6},
                            {'condition': 'light-rain',
                             'daytime': 'n',
                             'feels_like': 15,
                             'humidity': 97,
                             'icon': 'bkn_-ra_n',
                             'part_name': 'night',
                             'polar': False,
                             'prec_mm': 2.2,
                             'prec_period': 480,
                             'prec_prob': 20,
                             'pressure_mm': 751,
                             'pressure_pa': 1001,
                             'temp_avg': 15,
                             'temp_max': 16,
                             'temp_min': 13,
                             'wind_dir': 'w',
                             'wind_gust': 3.5,
                             'wind_speed': 1.8}],
                  'sunrise': '03:41',
                  'sunset': '20:53',
                  'week': 21},
     'info': {'lat': 57.626559,
              'lon': 39.893813,
              'url': 'https://yandex.ru/pogoda/16?lat=57.626559&lon=39.893813'},
     'now': 1685019651,
     'now_dt': '2023-05-25T13:00:51.228467Z'}


def get_weather_data():
    """Запрос данных от API Яндекс погоды."""
    url = 'https://api.weather.yandex.ru/v2/informers'
    key = str(os.getenv('YANDEX_WEATHER_KEY'))
    headers = {'X-Yandex-API-Key': key}
    params = {'lat': 57.626559, 'lon': 39.893813}
    weather_data = requests.get(url, headers=headers, params=params)
    return weather_data.json()


def parse_data(data):
    """Извлечение необходимых данных."""
    temperature = data['fact']['temp']
    condition = CONDITION_STATUS[data['fact']['condition']]
    icon = data['fact']['icon']
    return temperature, condition, icon


