from .base import BaseTeamsnapObject


class Statistics(BaseTeamsnapObject):
    rel = "statistics"
    type = "statistic"
    version = "3.866.0"

    __slots__ = [
        'acronym',
        'always_display_decimals',
        'formula',
        'is_in_descending_order',
        'display_zero_totals',
        'is_percentage',
        'is_private',
        'is_team_statistic',
        'is_top_statistic',
        'name',
        'precision',
        'statistic_group_id',
        'team_id',
    ]

