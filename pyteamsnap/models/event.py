from .base import BaseTeamsnapObject


class Event(BaseTeamsnapObject):
    """Associated object to a team; and represents an event or game that is tracked in the TeamSnap system.
    https://www.teamsnap.com/documentation/apiv3/objects#Events

    """

    rel = "events"
    type = "event"
    version = "3.866.0"

    __slots__ = [
        "additional_location_details",
        "arrival_date",
        "division_location_id",
        "doesnt_count_towards_record",
        "duration_in_minutes",
        "end_date",
        "formatted_results",
        "game_type",
        "game_type_code",
        "icon_color",
        "is_canceled",
        "is_game",
        "is_overtime",
        "is_shootout",
        "is_tbd",
        "label",
        "location_id",
        "minutes_to_arrive_early",
        "name",
        "notes",
        "opponent_id",
        "points_for_opponent",
        "points_for_team",
        "repeating_type",
        "repeating_type_code",
        "repeating_uuid",
        "results",
        "results_url",
        "shootout_points_for_opponent",
        "shootout_points_for_team",
        "start_date",
        "team_id",
        "time_zone",
        "time_zone_description",
        "time_zone_iana_name",
        "time_zone_offset",
        "source_time_zone_iana_name",
        "tracks_availability",
        "uniform",
        "is_league_controlled",
        "opponent_name",
        "location_name",
        "formatted_title",
        "formatted_title_for_multi_team",
        "created_at",
        "updated_at",
    ]

    def __str__(self):
        return f'{self.formatted_title}'
