class ApiServiceError(Exception):
    """Program received unsuitable response"""


class CantGetCoordinates(Exception):
    """Program couldn't obtain suitable coordinates"""
