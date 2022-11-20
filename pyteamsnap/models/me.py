from .user import User


class Me(User):
    """The current user's object. It is not possible to create or delete users via the API;
    however, it is possible to update data on a user's record.
    https://www.teamsnap.com/documentation/apiv3/objects#Me

    """

    rel = "me"
    type = "user"
    version = "3.866.0"
