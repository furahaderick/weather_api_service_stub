import logging

from app.exceptions import (
    CityNotFoundException,
    EmptyCityNameException,
    InvalidAPIKeyException,
)
from app.interfaces import WeatherProvider

logging.basicConfig(level=logging.INFO, format="%(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


class WeatherService:
    def __init__(self, provider: WeatherProvider) -> None:
        self.provider = provider
        self.valid_api_key = "super_secret_key"

    def get_city_forecast(self, city: str, api_key: str) -> dict[str, str | float]:

        if api_key != self.valid_api_key:
            logger.warning("Request with invalid API key received")
            raise InvalidAPIKeyException("Error: Unauthorized. Invalid key provided.")

        if not city or not city.strip():
            logger.warning("Request with empty city name received")
            raise EmptyCityNameException("Error: City name cannot be empty")

        data = self.provider.fetch(city)

        if data is None:
            logger.warning(
                "Request with unknown city name received", extra={"city_name": city}
            )
            raise CityNotFoundException(
                f"Sorry, weather data for '{city}' is currently unavailable"
            )

        return data
