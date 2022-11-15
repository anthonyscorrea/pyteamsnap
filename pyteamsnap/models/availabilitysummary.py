from .base import BaseApiObject


class AvailabilitySummary(BaseApiObject):
    rel = "availability_summaries"
    type = "availability_summary"
    version = "3.866.0"

    __slots__ = [
        "event_id",
        "team_id",
        "going_count",
        "not_going_count",
        "maybe_count",
        "unknown_count",
        "player_going_count",
        "player_not_going_count",
        "player_maybe_count",
        "player_unknown_count",
    ]
