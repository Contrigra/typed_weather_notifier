from typing import NamedTuple
from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class Coordinates(NamedTuple):
    latitude: float
    longitude: float


# TODO find and obtain my GPS data

def get_gps_coordinates() -> Coordinates:
    """Returns current coordinates using GPS app"""
    return Coordinates(longitude=10, latitude=20)


coordinates = get_gps_coordinates()
