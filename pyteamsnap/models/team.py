from .base import BaseApiObject


class Team(BaseApiObject):
    """Associated teams from your origin object. Full CRUD is possible with the teams endpoint.
    https://www.teamsnap.com/documentation/apiv3/objects#Teams


    """

    rel = "teams"
    type = "team"
    version = "3.866.0"

    # Override this class property to add docstring
    # should not change functionality. Probably a better
    # to do this...
    @property
    def data(self):
        """Data dictionary for object

        :return: dict: dict with keys:
        - ad_unit_hero_id
        - ad_unit_hero_template_id
        - ad_unit_inline_id
        - division_id
        - division_name
        - is_ownership_pending
        - league_name
        - league_url
        - location_country
        - location_postal_code
        - name
        - owner_email
        - owner_first_name
        - owner_last_name
        - season_name
        - sport_id
        - team
        - time_zone
        - type
        """
        return super().data
