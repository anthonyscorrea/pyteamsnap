from .base import BaseApiObject


class Availability(BaseApiObject):
    rel = "availabilities"
    type = "availability"
    version = "3.866.0"

    @property
    def data(self):
        """Data dictionary for object

        :return: dict: dict with keys:
        - event_id
        - member_id
        - notes
        - notes_author_member_id
        - source
        - status_code
        - type
        """
        return super().data
