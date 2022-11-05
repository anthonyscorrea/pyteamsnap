from .base import BaseApiObject


class EventLineup(BaseApiObject):
    rel = "event_lineups"
    type = "event_lineup"
    version = "3.866.0"
    template = {}

    @property
    def data(self):
        """
        :return: dict: dict with strings:
        """
        return super().data
