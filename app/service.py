from app.exceptions import (
    CityNotFoundException,
    EmptyCityNameException,
    InvalidAPIKeyException,
)
from app.interfaces import WeatherProvider


class WeatherService:
    def __init__(self, provider: WeatherProvider) -> None:
        self.provider = provider
        self.valid_api_key = "super_secret_key"

    def get_city_forecast(self, city: str, api_key: str) -> dict[str, str | float]:

        if api_key != self.valid_api_key:
            raise InvalidAPIKeyException("Error: Unauthorized. Invalid key provided.")

        if not city or not city.strip():
            raise EmptyCityNameException("Error: City name cannot be empty")

        data = self.provider.fetch(city)

        if data is None:
            raise CityNotFoundException(
                f"Sorry, weather data for '{city}' is currently unavailable"
            )

        return data
