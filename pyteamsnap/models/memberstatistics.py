from .base import BaseApiObject


class MemberStatistics(BaseApiObject):
    rel = "member_statistics"
    type = "member_statistic"

    __slots__ = [
        "id",
        "count_games_played",
        "total",
        "average",
        "total_ranking",
        "average_ranking",
        "total_ranking_for_query",
        "average_ranking_for_query",
        "statistic_id",
        "member_id",
        "team_id",
    ]
