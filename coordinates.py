from dataclasses import dataclass
import geocoder
import config


@dataclass(slots=True, frozen=True)
class Coordinates:
    latitude: float
    longitude: float


def get_gps_coordinates() -> Coordinates:
    """Returns current coordinates using geocoder app"""

    coordinates = _geocoder_get_coordinates_object()

    return _round_coordinates(coordinates=coordinates)


def _geocoder_get_coordinates_object() -> Coordinates:
    g = geocoder.ip('me')

    latitude, longitude = g.latlng
    coordinates = Coordinates(longitude=longitude, latitude=latitude)
    return coordinates


def _round_coordinates(coordinates: Coordinates) -> Coordinates:
    if config.USE_ROUNDED_COORDS:
        return Coordinates(*map(lambda c: round(c, 1),
                                [coordinates.latitude, coordinates.longitude]))
    else:
        return coordinates
