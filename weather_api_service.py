from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import TypeAlias, Literal

import requests

import config
from coordinates import Coordinates, get_gps_coordinates
from exceptions import ApiServiceError

Celsius: TypeAlias = int


class WeatherType(str, Enum):
    THUNDERSTORM = "Гроза"
    DRIZZLE = "Изморось"
    RAIN = "Дождь"
    SNOW = "Снег"
    CLEAR = "Ясно"
    FOG = "Туман"
    CLOUDS = "Облачно"


@dataclass(slots=True, frozen=True)
class Weather:
    temperature: Celsius
    weather_type: WeatherType
    sunrise: datetime
    sunset: datetime
    city: str


def get_weather(coordinates: Coordinates) -> Weather:
    """Requests weather in OpenWeatherApi and returns it"""
    openweather_response = _get_openweather_response(
        longitude=coordinates.longitude, latitude=coordinates.latitude)
    weather = _parse_openweather_response(openweather_response)

    return weather


def _get_openweather_response(longitude: float, latitude: float) -> dict:
    url = config.OPENWEATHER_URL.format(longitude=longitude, latitude=latitude)
    return requests.get(url).json()


def _parse_openweather_response(openweather_dict: dict) -> Weather:
    return Weather(temperature=_parse_temperature(openweather_dict),
                   weather_type=_parse_weather_type(openweather_dict),
                   sunrise=_parse_sun_time(openweather_dict, 'sunrise'),
                   sunset=_parse_sun_time(openweather_dict, 'sunset'))


def _parse_temperature(openweather_dict: dict) -> Celsius:
    return round(openweather_dict['main']['temp'])


def _parse_weather_type(openweather_dict: dict) -> WeatherType:
    try:
        weather_type_id = str(openweather_dict['weather'][0]['id'])
    except (IndexError, KeyError):
        raise ApiServiceError
    weather_types = {
        '1': WeatherType.THUNDERSTORM,
        '3': WeatherType.DRIZZLE,
        '5': WeatherType.RAIN,
        '6': WeatherType.SNOW,
        '7': WeatherType.FOG,
        '800': WeatherType.CLEAR,
        '80': WeatherType.CLOUDS
    }
    for _id, _weather_type in weather_types.items():
        if weather_type_id == _id:
            return _weather_type
    raise ApiServiceError


def _parse_sun_time(openweather_dict: dict,
                    time: Literal['sunrise'] | Literal['sunset']) -> datetime:
    pass


def _parse_city(openweather_dict: dict) -> str:
    pass


a = get_weather(get_gps_coordinates())
