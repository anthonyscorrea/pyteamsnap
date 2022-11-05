from .base import BaseApiObject


class EventLineupEntry(BaseApiObject):
    rel = "event_lineup_entries"
    type = "event_lineup_entry"
    version = "3.866.0"

    @property
    def data(self):
        """
        :return: dict: dict with strings:
        - member_id
        - sequence
        - label
        - type
        """
        return super().data

    @classmethod
    def search(cls, client, **kwargs):
        # For some reason the query listed for search at this endpoint is for EventLineup, not EventLineupEntry
        # this is a workaround
        r = client.get(f"{client.link(cls.rel)}/search", params=kwargs)
        results = client.parse_response(r)
        [cls(client, rel=cls.rel, data=r) for r in results]
        return [cls(client, rel=cls.rel, data=r) for r in results]
