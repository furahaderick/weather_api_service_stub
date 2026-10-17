from app.interfaces import WeatherProvider


class MockWeatherProvider(WeatherProvider):
    """Stores hard coded weather data"""

    def __init__(self) -> None:
        self._weather_database: dict[str, dict[str, str | float]] = {
            "kigali": {"temp": 24.5, "condition": "Sunny", "humidity": 65},
            "london": {"temp": 14, "condition": "Rainy", "humidity": 88},
            "new york": {"temp": 19.2, "condition": "Cloudy", "humidity": 70},
        }

    def fetch(self, city: str) -> dict[str, str | float] | None:
        return self._weather_database.get(city.lower())
