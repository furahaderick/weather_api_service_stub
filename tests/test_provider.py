from app.interfaces import WeatherProvider


def test_provider_returns_data(provider: WeatherProvider):
    kgl_data = provider.fetch("kigali")

    assert kgl_data is not None
    assert kgl_data == {"temp": 24.5, "condition": "Sunny", "humidity": 65}


def test_provider_returns_none_for_unknown_cities(provider: WeatherProvider):
    unknown_city_data = provider.fetch("mars_city")
    assert unknown_city_data is None


def test_provider_returns_none_for_empty_city_names(provider: WeatherProvider):
    empty_city_data = provider.fetch("  ")
    assert empty_city_data is None
