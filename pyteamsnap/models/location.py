from .base import BaseApiObject


class Location(BaseApiObject):
    rel = "locations"
    type = "location"
    version = "3.866.0"

    @property
    def data(self):
        """Data dictionary for object

        :return: dict: dict with keys:
        - name
        - url
        - phone
        - notes
        - address
        - latitude
        - longitude
        - team_id
        - is_retired
        - type
        """
        return super().data
