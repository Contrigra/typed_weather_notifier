class ApiServiceError(Exception):
    """Program received unsuitable response"""


class CantGetCoordinates(Exception):
    """Program couldn't obtain suitable coordinates"""


class CantWriteHistory(Exception):
    """Program couldn't manage to save history"""
