from .base import BaseTeamsnapObject, NotPossibleError


class User(BaseTeamsnapObject):

    rel = "users"
    type = "user"
    version = "3.866.0"

    __slots__ = [
        'first_name',
        'last_name',
        'password',
        'birthday',
        'email',
        'facebook_id',
        'facebook_access_token',
        'is_lab_rat',
        'receives_newsletter',
    ]

    def __str__(self):
        return f'{self["first_name"]} {self["last_name"]}'

    def delete(self):
        """It is not possible to create or delete users via the API;
            however, it is possible to update data on a user's record."""
        raise NotPossibleError ('It is not possible to delete users via the API')

    def new(self):
        """It is not possible to create or delete users via the API;
                    however, it is possible to update data on a user's record."""
        raise NotPossibleError('It is not possible to create users via the API')

    def post(self):
        """It is not possible to create or delete users via the API;
                    however, it is possible to update data on a user's record."""
        raise NotPossibleError('It is not possible to create users via the API')
