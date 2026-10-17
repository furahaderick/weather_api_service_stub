class InvalidAPIKeyException(Exception):
    """Raised when service receives an invalid api key"""


class CityNotFoundException(Exception):
    """Raised when a city is not found in our city database"""


class EmptyCityNameException(Exception):
    """Raised when service receives an empty city name as input"""
