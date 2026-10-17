import pytest

from app.exceptions import (
    CityNotFoundException,
    EmptyCityNameException,
    InvalidAPIKeyException,
)
from app.service import WeatherService


def test_service_uses_mock_data(service: WeatherService):

    result = service.get_city_forecast("kigali", "super_secret_key")

    assert result == {"temp": 24.5, "condition": "Sunny", "humidity": 65}


def test_service_rejects_invalid_api_key(service: WeatherService):
    with pytest.raises(
        InvalidAPIKeyException, match="Error: Unauthorized. Invalid key provided."
    ):
        _ = service.get_city_forecast("kigali", "invalid_api_key")


def test_service_rejects_empty_city_name(service: WeatherService):
    with pytest.raises(
        EmptyCityNameException, match="Error: City name cannot be empty"
    ):
        _ = service.get_city_forecast(" ", "super_secret_key")


def test_service_handles_unavailable_cities(service: WeatherService):
    with pytest.raises(
        CityNotFoundException,
        match="Sorry, weather data for 'mars_city' is currently unavailable",
    ):
        _ = service.get_city_forecast("mars_city", "super_secret_key")
