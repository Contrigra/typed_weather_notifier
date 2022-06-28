import urllib
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import TypeAlias

import requests

import config
from coordinates import Coordinates, get_gps_coordinates

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


def _parse_openweather_response(openweather_response: dict) -> Weather:
    pass


a = get_weather(get_gps_coordinates())