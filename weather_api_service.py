from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import TypeAlias

from coordinates import Coordinates

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

    return Weather(
        temperature=21,
        weather_type=WeatherType.CLEAR,
        sunrise=datetime.fromisoformat('2022-06-20 04:11:00'),
        sunset=datetime.fromisoformat('2022-06-20 21:15:00'),
        city='Saint_Petersburg'
    )
