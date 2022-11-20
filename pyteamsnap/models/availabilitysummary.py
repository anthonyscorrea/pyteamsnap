from .base import BaseTeamsnapObject


class AvailabilitySummary(BaseTeamsnapObject):
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

    def __str__(self):
        return f"{self.going_count} going, {self.maybe_count} maybe going, {self.not_going_count} not going, {self.unknown_count} unknown."
