from datetime import datetime

from exceptions import CantWriteHistory
from weather_api_service import Weather
from typing import Protocol
from pathlib import Path

from weather_formatter import format_weather


class WeatherStorage(Protocol):
    """Interface for any storage for saving weather data"""

    def save(self, weather: Weather) -> None:
        pass

class PlainFileWeatherStorage:
    """Store weather in plain text file"""
    def __init__(self, file: Path):
        self._file = file

    def save(self, weather: Weather) -> None:
        now = datetime.now()
        formatted_weather = format_weather(weather)
        try:
            with open(self._file, "a") as f:
                f.write(f"{now}\n{formatted_weather}\n")
        except OSError:
            raise CantWriteHistory

def save_weather(weather: Weather, storage: WeatherStorage) -> None:
    """Saves weather in a storage"""
    storage.save(weather)


