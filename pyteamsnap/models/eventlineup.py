from .base import BaseTeamsnapObject


class EventLineup(BaseTeamsnapObject):
    rel = "event_lineups"
    type = "event_lineup"
    version = "3.866.0"

    __slots__ = [
        "event_id",
        "is_published",
        "entries_count"
    ]
