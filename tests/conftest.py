# pylint: disable=redefined-outer-name

import pytest

from app.interfaces import WeatherProvider
from app.provider import MockWeatherProvider
from app.service import WeatherService


@pytest.fixture
def provider():
    return MockWeatherProvider()


@pytest.fixture
def service(provider: WeatherProvider):
    return WeatherService(provider=provider)
