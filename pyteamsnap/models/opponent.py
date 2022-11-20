from .base import BaseTeamsnapObject


class Opponent(BaseTeamsnapObject):
    rel = "opponents"
    type = "opponent"
    version = "3.866.0"

    __slots__ = [
        'name',
        'contacts_name',
        'contacts_phone',
        'contacts_email',
        'notes',
        'team_id',
    ]
