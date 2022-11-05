from .base import BaseApiObject


class Event(BaseApiObject):
    """Associated object to a team; and represents an event or game that is tracked in the TeamSnap system.
    https://www.teamsnap.com/documentation/apiv3/objects#Events

    """

    rel = "events"
    type = "event"
    version = "3.866.0"

    @property
    def data(self):
        """Data dictionary for object

        :return: dict: dict with strings:
        - type
        - additional_location_details
        - browser_time_zone
        - division_location_id
        - doesnt_count_towards_record
        - duration_in_minutes
        - game_type_code
        - icon_color
        - is_canceled
        - is_game
        - is_overtime
        - is_shootout
        - is_tbd
        - label
        - location_id
        - minutes_to_arrive_early
        - name
        - notes
        - notify_opponent
        - notify_opponent_contacts_email
        - notify_opponent_contacts_name
        - notify_opponent_notes
        - notify_team
        - notify_team_as_member_id
        - opponent_id
        - points_for_opponent
        - points_for_team
        - repeating_include
        - repeating_type_code
        - repeating_until
        - results
        - results_url
        - shootout_points_for_opponent
        - shootout_points_for_team
        - start_date
        - team_id
        - time_zone
        - tracks_availability
        - uniform
        """
        return super().data
