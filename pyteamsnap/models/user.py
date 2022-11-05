from .base import BaseApiObject


class User(BaseApiObject):
    rel = "users"
    type = "user"
    version = "3.866.0"

    def __str__(self):
        return f'{self["first_name"]} {self["last_name"]}'

    @property
    def data(self):
        """Data dictionary for object

        :return: dict: dict with keys:
        - first_name
        - last_name
        - password
        - birthday
        - email
        - facebook_id
        - facebook_access_token
        - type
        - is_lab_rat
        - receives_newsletter
        """
        return super().data
