from .base import BaseTeamsnapObject
from enum import Enum

class AvailabilityStatusCode(Enum):
    YES = 1
    MAYBE = 2
    NO = 0

class Availability(BaseTeamsnapObject):
    rel = "availabilities"
    type = "availability"
    version = "3.866.0"

    __slots__ = [
        "event_id",
        "member_id",
        "notes",
        "notes_author_member_id",
        "status",
        "status_code",
        "team_id",
        "is_current_user",
    ]

    def __str__(self):
        return self.data.get('status')

    def __repr__(self):
        return f'<TeamSnap {self.__class__.__name__} id={self.id} status_code={self.data.get("status_code")} status_="{self.data.get("status")}">'

    @classmethod
    def __sort_value(cls, availability_obj):
        if not isinstance(availability_obj, Availability):
            raise TypeError(f"Cannot compare type {availability_obj.__class__} with {cls.__class__}")
        return [
            AvailabilityStatusCode.YES.value,
            AvailabilityStatusCode.MAYBE.value,
            AvailabilityStatusCode.NO.value,
            None,
        ].index(availability_obj.status_code)

    def __lt__(self, obj):
        return (self.__sort_value(self) < (self.__sort_value(obj)))

    def __gt__(self, obj):
        return ((self.__sort_value(self)) > (self.__sort_value(obj)))

    def __le__(self, obj):
        return ((self.__sort_value(self)) <= (self.__sort_value(obj)))

    def __ge__(self, obj):
        return ((self.__sort_value(self)) >= (self.__sort_value(obj)))

    def __eq__(self, obj):

        return (self.__sort_value(self) == self.__sort_value(obj))
