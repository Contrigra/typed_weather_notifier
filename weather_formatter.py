from weather_api_service import Weather


def format_weather(weather: Weather) -> str:
    """Formats weather data in string"""
    return (f"{weather.city}, температура {weather.temperature}°C, "
            f"{weather.weather_type}\n"
            f"Восход: {weather.sunrise.strftime('%H:%M')}\n"
            f"Закат: {weather.sunset.strftime('%H:%M')}\n")


if __name__ == "__main__":
    from datetime import datetime
    from weather_api_service import WeatherType
    print(format_weather(Weather(
        temperature=15,
        weather_type=WeatherType.DRIZZLE,
        sunrise=datetime.fromisoformat("2022-06-25 03:30:00"),
        sunset=datetime.fromisoformat("2022-06-25 21:00:00"),
        city="Irkutsk"
    )))
