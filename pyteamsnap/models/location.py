from .base import BaseApiObject


class Location(BaseApiObject):
    rel = "locations"
    type = "location"
    version = "3.866.0"

    __slots__ = [
        'name',
        'url',
        'phone',
        'notes',
        'address',
        'latitude',
        'longitude',
        'team_id',
        'is_retired',
    ]
