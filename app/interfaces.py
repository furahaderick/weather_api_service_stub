from abc import ABC, abstractmethod


class WeatherProvider(ABC):
    @abstractmethod
    def fetch(self, city: str) -> dict[str, str | float] | None: ...
