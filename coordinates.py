from typing import NamedTuple
from dataclasses import dataclass
import geocoder


@dataclass(frozen=True)
class Coordinates(NamedTuple):
    latitude: float
    longitude: float


# TODO find and obtain my GPS data

def get_gps_coordinates() -> Coordinates:
    """Returns current coordinates using geocoder app"""

    g = geocoder.ip('me')
    latitude, longitude = g.latlng

    return Coordinates(longitude=longitude, latitude=longitude)
