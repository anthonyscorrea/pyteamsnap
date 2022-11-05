from .base import BaseApiObject


class Opponent(BaseApiObject):
    rel = "opponents"
    type = "opponent"
    version = "3.866.0"

    @property
    def data(self):
        """Data dictionary for object

        :return: dict: dict with keys:
        - name
        - contacts_name
        - contacts_phone
        - contacts_email
        - notes
        - team_id
        - type
        """
        return super().data
