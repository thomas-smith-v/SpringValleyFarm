import requests
from dateutil import parser
from datetime import datetime
import pytz

FARM_WEATHER_API = "https://api.weather.gov/gridpoints/BOX/33,44"
HEADERS = {"User-Agent": "SpringValleyFarm"}

def get_weather():
    return requests.get(FARM_WEATHER_API, headers=HEADERS).json()

def get_temperature_forecast(weather:dict=None):
    if not weather:
        weather = get_weather()

    values = weather['properties']['temperature']['values']
    
    for value in values:
        value['validTime'] =  _parse_time(value['validTime']).isoformat()
        value['value'] = _convert_to_f(value['value'])

    return values

def get_sky_cover_forecast(weather:dict=None):
    if not weather:
        weather = get_weather()

    values = weather['properties']['skyCover']['values']

    for value in values:
        value['validTime'] =  _parse_time(value['validTime']).isoformat()

    return values

def _parse_time(time_string: str):
    return parser.isoparse(time_string.split("/")[0]).astimezone(tz=pytz.timezone("US/Eastern"))

def _convert_to_f(c: float):
    return (c * (9/5)) + 32

def get_current(values: dict):
    """
    Values should be in the format of:
    {
        "validTime": time string,
        "value": number
    }
    """
    return min(values, key=lambda x: abs(_parse_time(x['validTime']) - datetime.now().astimezone(tz=pytz.timezone("US/Eastern"))))['value']

print(get_current(get_temperature_forecast()))