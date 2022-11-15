from .base import BaseApiObject


class Opponent(BaseApiObject):
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
