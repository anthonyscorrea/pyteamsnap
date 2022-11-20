from .base import BaseTeamsnapObject


class Member(BaseTeamsnapObject):
    """A member (also referred to as a roster in our web and mobile apps) is a member of a team.
    https://www.teamsnap.com/documentation/apiv3/objects#Members

    """

    rel = "members"
    type = "member"
    version = "3.866.0"

    __slots__ = [
        'first_name',
        'last_name',
        'address_city',
        'address_state',
        'address_street1',
        'address_street2',
        'address_zip',
        'birthday',
        'gender',
        'hide_address',
        'hide_age',
        'is_address_hidden',
        'is_age_hidden',
        'is_manager',
        'is_non_player',
        'is_ownership_pending',
        'jersey_number',
        'position',
        'source_action',
        'team_id',
    ]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
