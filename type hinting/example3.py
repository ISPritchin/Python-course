from dataclasses import dataclass
from typing import TypedDict


@dataclass
class Coordinates(TypedDict):
    longitude: float
    latitude: float


def get_gps_coordinates() \
        -> Coordinates:
    """Returns current coordinates"""
    return Coordinates(**{"latitude": 10.0, "longitude": 20.0})