from abc import ABC, abstractmethod


class WeatherProvider(ABC):
    """Defines the weather provider interface or contract"""

    @abstractmethod
    def fetch(self, city: str) -> dict[str, str | float] | None: ...
