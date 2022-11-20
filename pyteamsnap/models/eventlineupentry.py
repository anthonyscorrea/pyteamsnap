from .base import BaseTeamsnapObject


class EventLineupEntry(BaseTeamsnapObject):
    rel = "event_lineup_entries"
    type = "event_lineup_entry"
    version = "3.866.0"

    __slots__ = [
        "event_lineup_id",
        "event_id",
        "member_id",
        "sequence",
        "label",
        "member_name",
        "member_photo",
        "availability_status_code"
    ]

    @classmethod
    def search(cls, client, **kwargs):
        # For some reason the query listed for search at this endpoint is for EventLineup, not EventLineupEntry
        # this is a workaround
        r = client.get(f"{client.link(cls.rel)}/search", params=kwargs)
        results = client.parse_response(r)
        [cls(client, data=r) for r in results]
        return [cls(client, data=r) for r in results]
